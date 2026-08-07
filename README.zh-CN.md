[English](./README.md) | **中文**

# teamai-cli 后端工程师参考模板

## 如何使用

安装 teamai-cli:
```sh
npm install -g teamai-cli
```

点击本页顶部的 **Use this template**,在你所在团队的 git 目录下生成自己的仓库(history 干净、无 fork 关系),然后用它初始化 teamai-cli:
```sh
teamai init https://github.com/<你的-org>/<你的-repo>
```

- 也可直接将这个文件的内容及你的新仓库交给 AI 安装、初始化

## 模板内置的数据

### skills

按上游来源分命名空间存放（详见下方「来源与许可」）：

- **`skills/ecc/`**（后端内容型）：`backend-patterns`、`api-design`、
  `database-migrations`、`error-handling`、`tdd-workflow`、`security-review`。
- **`skills/mattpocock/`**（工程方法型）：`tdd`、`research`、`domain-modeling`、
  `grill-me` + `grilling`（配套：反复追问、逐个敲定方案决策）。

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

- MIT 许可原文见 [`LICENSE`](./LICENSE)（ECC）及 [`skills/mattpocock/LICENSE`](./skills/mattpocock/LICENSE)。
- 每个文件与上游的路径对应关系见 [`ATTRIBUTION.md`](./ATTRIBUTION.md)。

> 本仓库收录的内容均为 MIT 许可，可按 MIT 条款复制、修改、再分发；请保留版权与许可声明。

### 如有建议请直接提 issue/PR
