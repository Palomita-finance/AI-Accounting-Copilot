from src.metrics import calculate_metrics
from src.analyzer import detect_abnormal_expense
from src.trend import analyze_trend
from src.insight import generate_insight


def metrics_tool(context):

    result = calculate_metrics(
        context.data
    )

    context.metrics = result

    return {
        "tool": "metrics_tool",
        "success": True,
        "data": result
    }


def abnormal_tool(context):

    result = detect_abnormal_expense(
        context.data
    )

    context.abnormal = result

    return {
        "tool": "abnormal_tool",
        "success": True,
        "data": result
    }


def trend_tool(context):

    result = analyze_trend(
        context.data
    )

    context.trend = result

    return {
        "tool": "trend_tool",
        "success": True,
        "data": result
    }


def insight_tool(context):
    """
    根据财务分析结果生成业务建议
    """

    result = generate_insight(
        context.metrics,
        len(context.abnormal)
    )

    context.insights = result

    return {
        "tool": "insight_tool",
        "success": True,
        "data": result
    }
