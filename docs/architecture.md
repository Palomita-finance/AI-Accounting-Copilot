# AI Accounting Copilot V1 架构

`main.py` 读取数据并把用户问题交给 `src/agent/agent_loop.py`。Router 根据问题和 Context 决定工具；Loop 校验固定依赖顺序并防止重复；Executor 调用 `metrics`、`analyzer`、`trend`、`insight` 核心能力；每个成功结果保存到 Context；全部分析工具完成后，`agent_response.py` 生成最终 AI 回答。

```text
User -> Router -> Loop -> Executor -> Tools -> Context
                                      |
                                      v
                              Final AI Response
```

`src/report.py` 是独立可选文本导出模块，不在 Agent 工具注册表中。
