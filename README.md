# teamai-cli 后端工程师参考模板

## 如何使用

安装 teamai-cli，
```sh
npm install -g teamai-cli
```

将此仓库 fork 到你所在团队的 git 目录下（需要确保团队成员都是 master），并用 fork 后的仓库初始化 teamai-cli
```sh
teamai init --repo https://github.com/Your-fork-org/team-template
```

- 也可直接将这个文件的内容及你 fork 的仓库交给 AI 安装、初始化

## 模板内置的数据

### skills

按上游来源分命名空间存放（详见下方「来源与许可」）：

- **`skills/ecc/`**（后端内容型）：`backend-patterns`、`api-design`、
  `database-migrations`、`error-handling`、`tdd-workflow`、`security-review`。
- **`skills/mattpocock/`**（工程方法型）：`tdd`、`research`、`domain-modeling`、
  `grill-me` + `grilling`（配套：反复追问、逐个敲定方案决策）。
- **`skills/karpathy/`**（⚠️ 上游无 license，仅供内部评审，公开分发前须先确认授权）：
  `karpathy-guidelines`。

### rules

- **全员共享基线**（`rules/common/`）：编码风格、代码评审、测试、Git 工作流、安全、
  性能等（来源见下方「来源与许可」）。

### agents

- **后端评审子代理**：`code-reviewer`、`database-reviewer`、`security-reviewer`
  （来源见下方「来源与许可」）。

### 环境变量

仅作示例，管理员可自行调整团队级的环境变量。

## 来源与许可

本模板内容改编自多个开源项目，按来源分命名空间存放：

| 命名空间 | 上游 | 许可 |
|---|---|---|
| `skills/ecc/`、`rules/common/`、`agents/` | [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | ✅ MIT |
| `skills/mattpocock/` | [mattpocock/skills](https://github.com/mattpocock/skills) | ✅ MIT |
| `skills/karpathy/` | [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | ⚠️ **无 license** |

- MIT 许可原文见 [`LICENSE`](./LICENSE)（ECC）及 [`skills/mattpocock/LICENSE`](./skills/mattpocock/LICENSE)。
- 每个文件与上游的路径对应关系见 [`ATTRIBUTION.md`](./ATTRIBUTION.md)。

> ⚠️ **`skills/karpathy/` 上游未声明 license**，默认保留全部版权。当前仅在此私密仓库内供评审，
> **公开分发前必须先取得授权或改为链接引用**，不可直接复制分发。
>
> MIT 部分的复制、修改、再分发均遵循 MIT 条款；请保留版权与许可声明。

### 如有建议请直接提 issue/PR
