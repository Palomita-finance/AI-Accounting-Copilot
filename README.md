# AI Accounting Copilot V1

一个基于 LLM Router 和工具调用循环的财务分析 Agent。它读取 Excel 财务数据，依次计算核心指标、检测异常支出、分析月度趋势、生成业务洞察，最后由 AI 汇总为中文分析结果。

## Agent 流程

```text
用户问题 -> LLM Router -> Agent Loop -> Tool Executor
         -> Context 保存状态 -> AI Response 生成最终回答
```

工具按依赖顺序执行：`metrics_tool -> abnormal_tool -> trend_tool -> insight_tool -> finish`。成功执行的工具才会写入 `completed_tools`，循环会阻止重复和越级调用。

## 运行

1. 安装依赖：`pip install -r requirements.txt`
2. 在 `.env` 配置 `DEEPSEEK_API_KEY`
3. 运行：`python main.py`
4. 测试：`python -m unittest discover -s tests -v`

默认示例数据位于 `data/demo_financial_data.xlsx`。

## 项目结构

```text
AI-Accounting-Copilot/
├── data/
├── docs/
├── src/
│   ├── agent/
│   │   ├── agent_executor.py
│   │   ├── agent_loop.py
│   │   ├── agent_response.py
│   │   ├── context.py
│   │   ├── llm_router.py
│   │   └── tools.py
│   ├── ai_analyzer.py
│   ├── analyzer.py
│   ├── insight.py
│   ├── metrics.py
│   ├── report.py
│   └── trend.py
├── tests/
├── config.py
├── generate_test_data.py
├── main.py
└── requirements.txt
```

`report.py` 仅保留为可选的文本导出能力，不参与 Agent 主流程，避免与 `agent_response.py` 重复生成报告。
