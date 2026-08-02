import pandas as pd
import streamlit as st

from src.agent.agent_executor import execute_tool
from src.agent.context import AgentContext


TOOL_PIPELINE = (
    ("metrics_tool", "Metrics analysis"),
    ("abnormal_tool", "Abnormal detection"),
    ("trend_tool", "Trend analysis"),
    ("insight_tool", "Insight generation"),
)


def build_dashboard_context(data, question):
    """Build a Web presentation context with the existing financial tools."""

    context = AgentContext(data, question)

    for tool_name, _ in TOOL_PIPELINE:
        try:
            result = execute_tool(tool_name, context)
        except Exception as exc:
            result = {
                "tool": tool_name,
                "success": False,
                "error": str(exc),
            }

        context.history.append(result)
        if result.get("success") is True:
            context.completed_tools.append(tool_name)

    return context


def render_dashboard(context):
    render_metrics(context.metrics)
    render_pipeline(context.completed_tools)

    trend_column, abnormal_column = st.columns([1, 1], gap="large")
    with trend_column:
        render_trend(context.trend)
    with abnormal_column:
        render_abnormal(context.abnormal)


def render_metrics(metrics):
    st.markdown("## Financial dashboard")

    if not metrics:
        st.info("财务指标尚未生成。", icon=":material/info:")
        return

    cards = st.columns(4, gap="medium")
    cards[0].metric(
        "Revenue",
        format_currency(metrics.get("总收入")),
        border=True,
    )
    cards[1].metric(
        "Expense",
        format_currency(metrics.get("总支出")),
        border=True,
    )
    cards[2].metric(
        "Profit",
        format_currency(metrics.get("利润")),
        border=True,
    )

    profit_margin = metrics.get("利润率")
    margin_text = "无法计算" if profit_margin is None else f"{profit_margin:.2%}"
    cards[3].metric("Profit margin", margin_text, border=True)


def render_pipeline(completed_tools):
    with st.container(border=True):
        st.subheader("Agent analysis pipeline")
        completed = set(completed_tools)

        for tool_name, label in TOOL_PIPELINE:
            if tool_name in completed:
                st.markdown(f":material/check_circle: **{label}**")
            else:
                st.markdown(f":material/pending: {label}")

        if all(tool_name in completed for tool_name, _ in TOOL_PIPELINE):
            st.markdown(":material/smart_toy: **AI financial diagnosis**")
        else:
            st.markdown(":material/hourglass_top: AI financial diagnosis")


def render_trend(trend):
    with st.container(border=True, height="stretch"):
        st.subheader("Monthly expense trend")

        if trend is None or len(trend) == 0:
            st.info("暂无趋势数据。", icon=":material/info:")
            return

        trend_data = pd.DataFrame(
            {
                "月份": [f"{month}月" for month in trend.index],
                "支出金额": trend.values,
            }
        )
        st.line_chart(
            trend_data,
            x="月份",
            y="支出金额",
            x_label="月份",
            y_label="支出金额（¥）",
            height=360,
        )


def render_abnormal(abnormal):
    with st.container(border=True, height="stretch"):
        st.subheader("Detected abnormal transactions")

        if abnormal is None or abnormal.empty:
            st.success("未检测到异常交易。", icon=":material/check_circle:")
            return

        display_columns = [
            column
            for column in ("日期", "摘要", "类别", "支出")
            if column in abnormal.columns
        ]
        display_data = abnormal.loc[:, display_columns].copy()

        st.caption(f"共检测到 {len(display_data):,} 笔异常交易")
        st.dataframe(
            display_data,
            hide_index=True,
            height=360,
            column_config={
                "日期": st.column_config.DateColumn("日期", format="YYYY-MM-DD"),
                "支出": st.column_config.NumberColumn("支出", format="¥%,.0f"),
            },
            key="abnormal_transactions",
        )


def format_currency(value):
    if value is None:
        return "N/A"

    amount = float(value)
    if amount < 0:
        return f"-¥{abs(amount):,.0f}"
    return f"¥{amount:,.0f}"
