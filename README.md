**English** | [中文](./README.zh-CN.md)

# teamai-cli Backend Engineer Reference Template

## Usage

Install teamai-cli:
```sh
npm install -g teamai-cli
```

Click **Use this template** at the top of this page to create your own repo (clean history, no fork link) in your team's namespace, then initialize teamai-cli against it:
```sh
teamai init https://github.com/<your-org>/<your-repo>
```

- Alternatively, hand this file and your new repo to an AI to install and initialize for you.

## What's in the template

### skills

Organized into namespaces by upstream source (see "Sources & License" below):

- **`skills/ecc/`** (backend content): `backend-patterns`, `api-design`,
  `database-migrations`, `error-handling`, `tdd-workflow`, `security-review`.
- **`skills/mattpocock/`** (engineering methodology): `tdd`, `research`, `domain-modeling`,
  `grill-me` + `grilling` (a pair: relentless questioning to nail down design decisions).

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

- Full MIT license text: [`LICENSE`](./LICENSE) (ECC) and [`skills/mattpocock/LICENSE`](./skills/mattpocock/LICENSE).
- Per-file upstream path mapping: [`ATTRIBUTION.md`](./ATTRIBUTION.md).

> All bundled content is MIT-licensed. It may be copied, modified, and redistributed under
> MIT terms; retain the copyright and license notices.

### Suggestions? Open an issue / PR.
