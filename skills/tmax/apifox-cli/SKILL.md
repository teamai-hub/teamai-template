---
name: apifox-cli
description: "This skill should be used when operating Apifox via the apifox-cli (token login, importing/exporting API definitions, adding common parameters) — especially from a markdown API doc into a project. It captures the two recurring sandbox traps: (1) the Bash token login command, and (2) the mandatory proxy removal without which every network command returns a fake 400 'invalid token'."
---

# Apifox CLI Operations

## Overview

Operate the Apifox CLI (`apifox`) to log in with a personal access token, locate a team/project, import API definitions (typically generated from a markdown spec via OpenAPI 3.x), and add project-level common parameters (e.g. an auth request header). All steps run on the command line — no GUI needed except one-time permission toggles.

**Two traps are non-negotiable and the whole reason this skill exists — read them first:**

### 🔴 TRAP 1 — Proxy MUST be stripped on every network command

The WorkBuddy sandbox forces all egress through a local intercepting proxy:

```
HTTP_PROXY=http://127.0.0.1:56871
HTTPS_PROXY=http://127.0.0.1:56871
```

This proxy **rewrites HTTPS requests to apifox**, so the server receives a mangled request and rejects it with `400` / "请检查访问令牌后重试" even though the token is perfectly valid. This looks exactly like an invalid-token error and will mislead you into blaming the token.

**Rule:** Prefix EVERY apifox command that touches the network with proxy removal. Do not trust a `400`; first retry with the proxy stripped before concluding the token is bad.

```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy apifox <subcommand>
```

A ready-made wrapper is provided at `scripts/apifox.sh` — call it as `bash <skill>/scripts/apifox.sh <subcommand>` and it strips the proxy for you. Keep `export PATH="/Users/mk/.npm-global/bin:$PATH"` so the `apifox` binary resolves.

### 🔴 TRAP 2 — Bash token login

Login with a personal access token (not interactive browser login, which won't work in the sandbox):

```bash
export PATH="/Users/mk/.npm-global/bin:$PATH"
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy \
  apifox auth login --with-token afxp_XXXX
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy apifox auth whoami
```

- The token is persisted to `~/.apifox/config.toml`; no need to re-login each session unless the token is revoked.
- If `whoami` returns `400`, that is TRAP 1, not a bad token — re-run with the proxy stripped. (This is the exact mistake to avoid: the user's own machine has no such proxy, so the same token works there directly.)
- `apifox --version` / `npm i -g apifox-cli` to (re)install or upgrade.

## Workflow

### Step 1 — Locate team and project

```bash
# list teams, find the target team name -> teamId
bash <skill>/scripts/apifox.sh team list
# list projects, find target project name -> projectId
bash <skill>/scripts/apifox.sh project list
# confirm project belongs to that team (teamId field) and check current endpointCount
bash <skill>/scripts/apifox.sh project get <projectId>
```

Only `projectId` (a numeric id, NOT the name) is used by `import` / `endpoint` / `common-parameter` commands.

### Step 2 — Generate an OpenAPI 3.x file from the markdown doc

Apifox's `import` accepts OpenAPI 3.x and is the most reliable way to create many endpoints with full field/enum/example detail in one shot. Build the OpenAPI JSON by reading the markdown and mapping each endpoint to a `paths` entry, each request/response body to a `components.schemas` model.

Use the scaffolding in `scripts/build_openapi.py` as a starting point: it provides helper functions (`resp_200`, `errs`, `body`, `query`, etc.) and a clear place to append `paths[...]`. Run:

```bash
python3 scripts/build_openapi.py <input.md> -o /tmp/out.openapi.json
```

Then validate it is well-formed JSON and count operations:

```bash
python3 -c "import json;d=json.load(open('/tmp/out.openapi.json'));print('ops',sum(len(v) for v in d['paths'].values()))"
```

**Pitfall:** if a path has two methods (e.g. GET + POST on the same path), build the dict by merging methods on one key — do NOT assign each method to a separate `paths[path]` assignment, or the later one silently overwrites the earlier (you'd lose an operation and see a count one short).

### Step 3 — Import into the project

```bash
bash <skill>/scripts/apifox.sh import \
  --project <projectId> --format openapi --file /tmp/out.openapi.json
```

- Expect output like `createCount: N, folder createCount: M, errorCount: 0`. Folders become Apifox modules grouped by the OpenAPI `tags`.
- **AI write protection:** Apifox (≥ 2.8.32) blocks external/AI edits unless the project setting **项目设置 → 功能设置 → 外部 AI 编辑权限** is enabled for the main branch. If import fails with `Automation caller branch required`, either (a) ask the user to enable that permission in the GUI and retry, or (b) create an AI branch and import into it for later review/merge. Do NOT assume — confirm the approach with the user.

### Step 4 — Verify

```bash
bash <skill>/scripts/apifox.sh endpoint list --project <projectId> --page 1 --page-size 500
```

- Trust `endpoint list` as the source of truth for endpoint count. Note `project get` may report a stale `endpointCount: 0` (a CLI statistics cache quirk) even after a successful import — do not be alarmed.
- Confirm the module/folder names match the markdown grouping via `bash <skill>/scripts/apifox.sh folder list --project <projectId>`.

### Step 5 — Add a project-level common parameter (e.g. auth header)

To apply a request header (auth, tracing, etc.) to ALL endpoints at once, use a project-level common parameter rather than editing 16 endpoints individually.

1. Get the exact schema first (never guess field names/enums):
   ```bash
   bash <skill>/scripts/apifox.sh cli-schema get common-parameter-create
   ```
2. Write a JSON file per the template in `references/common-parameter.md` (header item with `name`, `defaultValue`, `required`, `defaultEnable`, `enable`, `type`).
3. Validate then create:
   ```bash
   bash <skill>/scripts/apifox.sh cli-schema validate common-parameter-create --file /tmp/cp.json
   bash <skill>/scripts/apifox.sh common-parameter create --project <projectId> --file /tmp/cp.json
   ```
4. Verify inheritance: `common-parameter list --project <projectId>` shows it; each endpoint's own `commonParameters` field will be `{}` meaning "inherit project default (and it's enabled)". The header appears in every endpoint's "公共参数（继承）" section, auto-applied.

## Resources

### scripts/apifox.sh
Drop-in wrapper that runs `apifox` with the sandbox intercepting proxy removed. Use it for every network command. Usage: `bash <skill-dir>/scripts/apifox.sh <any apifox subcommand and args>`.

### scripts/build_openapi.py
Reusable OpenAPI 3.x generator scaffolding. Provides helpers to declare responses, error blocks, request bodies, and query params, plus a clear `paths` section to populate from the markdown. Adapt the path/schema section per document.

### references/common-parameter.md
JSON template and field notes for the `common-parameter create` payload (adding a header to all endpoints).

### references/openapi-generation.md
Detailed notes on mapping a markdown API doc into OpenAPI 3.x (grouping into tags/modules, modeling enums, examples, and the multi-method-same-path pitfall).
