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

- **GitHub 开源的热门后端 skill**（来源见下方「来源与许可」）：
  `backend-patterns`、`api-design`、`database-migrations`、`error-handling`、
  `tdd-workflow`、`security-review`。

### rules

- **全员共享基线**（`rules/common/`）：编码风格、代码评审、测试、Git 工作流、安全、
  性能等（来源见下方「来源与许可」）。

### agents

- **后端评审子代理**：`code-reviewer`、`database-reviewer`、`security-reviewer`
  （来源见下方「来源与许可」）。

### 环境变量

仅作示例，管理员可自行调整团队级的环境变量。

## 来源与许可

本模板内的 `skills/`、`rules/`、`agents/` 内容改编自开源项目
[everything-claude-code](https://github.com/affaan-m/everything-claude-code)（作者 Affaan Mustafa，**MIT 许可**）。

- 完整 MIT 许可原文见 [`LICENSE`](./LICENSE)。
- 每个文件与上游的路径对应关系见 [`ATTRIBUTION.md`](./ATTRIBUTION.md)。

> 复制、修改、再分发均遵循 MIT 条款；请保留上述版权与许可声明。

### 如有建议请直接提 issue/PR
