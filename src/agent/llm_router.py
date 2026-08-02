import json

from src.ai_analyzer import client


def choose_tool_with_llm(question, context):

    prompt = f"""
你是一个财务分析Agent，负责决定下一步动作。

用户问题：
{question}


====================
可用工具
====================


1. metrics_tool

功能：
计算收入、支出、利润、利润率、最大支出类别等基础指标。


2. abnormal_tool

功能：
检测异常交易、大额支出和潜在风险。


3. trend_tool

功能：
分析月份之间收入或支出的变化趋势。


4. insight_tool

功能：
根据财务指标、异常交易、趋势分析结果，
生成专业财务分析建议。


====================
工具调用规则
====================

1. metrics_tool

通常应该最先调用，
用于获取基础财务指标。


2. abnormal_tool

通常在 metrics_tool 后调用，
用于分析风险交易。


3. trend_tool

通常在 metrics_tool 后调用，
用于分析变化趋势。


4. insight_tool

只有在以下工具完成后才能调用：

- metrics_tool
- abnormal_tool
- trend_tool


====================
当前状态
====================

已经完成的工具：

{context.completed_tools}


已有分析结果：

metrics:
{context.metrics}


abnormal:
{context.abnormal}


trend:
{context.trend}


insights:
{context.insights}



====================
决策规则
====================

1.
不要重复调用已经完成的工具。


2.
如果所有分析任务已经完成，
返回：

{{
    "action": "finish",
    "tool": null
}}


3.
如果需要调用工具：

返回：

{{
    "action": "tool",
    "tool": "工具名称"
}}


4.
如果已经拥有足够信息，可以直接回答：

返回：

{{
    "action": "answer",
    "tool": null
}}



====================
重要要求
====================

1. 只能返回JSON。

2. 不要输出任何解释。

3. tool字段只能填写以下之一：

metrics_tool
abnormal_tool
trend_tool
insight_tool

4. action只能是：

tool
answer
finish


现在判断下一步动作。
"""

    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    result = response.choices[0].message.content.strip()

    if result.startswith("```"):
        result = result.removeprefix("```json").removeprefix("```")
        result = result.removesuffix("```").strip()

    decision = json.loads(result)

    if decision.get("action") not in {"tool", "answer", "finish"}:
        raise ValueError("LLM返回了无效action")

    allowed_tools = {
        "metrics_tool",
        "abnormal_tool",
        "trend_tool",
        "insight_tool"
    }

    if (
        decision.get("action") == "tool"
        and decision.get("tool") not in allowed_tools
    ):
        raise ValueError("LLM返回了无效工具")

    return decision
