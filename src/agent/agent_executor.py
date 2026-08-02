from src.agent.tools import (
    metrics_tool,
    abnormal_tool,
    trend_tool,
    insight_tool
)


def execute_tool(tool_name, context):

    if tool_name == "metrics_tool":

        return metrics_tool(context)

    elif tool_name == "abnormal_tool":

        return abnormal_tool(context)

    elif tool_name == "trend_tool":

        return trend_tool(context)

    elif tool_name == "insight_tool":

        return insight_tool(context)

    return {
        "tool": tool_name,
        "success": False,
        "error": f"未知工具: {tool_name}"
    }
