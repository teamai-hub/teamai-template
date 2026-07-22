**English** | [中文](./README.zh-CN.md)

# teamai-cli Backend Engineer Reference Template

## Usage

Install teamai-cli:
```sh
npm install -g teamai-cli
```

Fork this repository into your team's git namespace (make sure all team members are `master`), then initialize teamai-cli with your fork:
```sh
teamai init --repo https://github.com/Your-fork-org/template-backend
```

- Alternatively, hand this file and your forked repo to an AI to install and initialize for you.

## What's in the template

### skills

Organized into namespaces by upstream source (see "Sources & License" below):

- **`skills/ecc/`** (backend content): `backend-patterns`, `api-design`,
  `database-migrations`, `error-handling`, `tdd-workflow`, `security-review`.
- **`skills/mattpocock/`** (engineering methodology): `tdd`, `research`, `domain-modeling`,
  `grill-me` + `grilling` (a pair: relentless questioning to nail down design decisions).
- **`skills/karpathy/`** (⚠️ no upstream license — internal review only; confirm authorization
  before public distribution): `karpathy-guidelines`.

### rules

- **Shared baseline for everyone** (`rules/common/`): coding style, code review, testing,
  Git workflow, security, performance, and more (source below).

### agents

- **Backend review subagents**: `code-reviewer`, `database-reviewer`, `security-reviewer`
  (source below).

### Environment variables

Examples only — admins can adjust team-level environment variables as needed.

## Sources & License

The content here is adapted from several open-source projects, organized into namespaces by source:

| Namespace | Upstream | License |
|---|---|---|
| `skills/ecc/`, `rules/common/`, `agents/` | [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | ✅ MIT |
| `skills/mattpocock/` | [mattpocock/skills](https://github.com/mattpocock/skills) | ✅ MIT |
| `skills/karpathy/` | [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | ⚠️ **NONE** |

- Full MIT license text: [`LICENSE`](./LICENSE) (ECC) and [`skills/mattpocock/LICENSE`](./skills/mattpocock/LICENSE).
- Per-file upstream path mapping: [`ATTRIBUTION.md`](./ATTRIBUTION.md).

> ⚠️ **`skills/karpathy/` has no license declared upstream** — all rights reserved by default.
> It is included here **only for private review**. **Confirm authorization or switch to a
> reference/link before any public distribution**; do not copy or redistribute it as-is.
>
> The MIT-licensed content may be copied, modified, and redistributed under MIT terms;
> retain the copyright and license notices.

### Suggestions? Open an issue / PR.
