import streamlit as st

from src.agent.agent_loop import run_agent
from src.data_loader import load_excel
from src.web.dashboard import build_dashboard_context, render_dashboard
from src.web.report_view import render_report
from src.web.ui_components import (
    REQUIRED_COLUMNS,
    render_file_summary,
    render_header,
    render_sidebar,
)


st.set_page_config(
    page_title="AI Accounting Copilot",
    page_icon="📊",
    layout="wide",
)

st.session_state.setdefault("analysis_answer", None)
st.session_state.setdefault("analysis_context", None)

render_sidebar()
render_header()

with st.container(border=True):
    st.subheader("上传 Excel 财务数据")
    uploaded_file = st.file_uploader(
        "选择 Excel 文件",
        type=["xlsx", "xls"],
        help="字段要求：日期 | 摘要 | 类别 | 收入 | 支出",
        key="financial_file",
    )

data = None
missing_columns = set()
file_error = None

if uploaded_file is not None:
    try:
        data = load_excel(uploaded_file)
        missing_columns = REQUIRED_COLUMNS - set(data.columns)
    except Exception as exc:
        file_error = exc

render_file_summary(uploaded_file, data, missing_columns, file_error)

question = st.text_input(
    "分析问题",
    value="请分析公司的财务风险和经营问题",
    key="analysis_question",
)

analyze = st.button(
    "开始分析",
    type="primary",
    icon=":material/analytics:",
    width="stretch",
)

if analyze:
    st.session_state.analysis_answer = None
    st.session_state.analysis_context = None

    if uploaded_file is None:
        st.warning("请先上传 Excel 文件。", icon=":material/warning:")
    elif file_error is not None:
        st.error(
            "Excel 文件读取失败，请确认文件未损坏且格式正确。",
            icon=":material/error:",
        )
    elif missing_columns:
        st.error("❌ Excel格式错误，请检查字段。", icon=":material/error:")
    elif not question.strip():
        st.warning("请输入需要分析的问题。", icon=":material/warning:")
    else:
        try:
            with st.status(
                "Agent 正在分析财务数据...",
                expanded=True,
            ) as status:
                st.write("LLM Router 正在规划财务工具调用流程")
                answer = run_agent(data.copy(), question.strip())
                st.write("Financial Tools 执行完成，正在整理 Dashboard 数据")
                dashboard_context = build_dashboard_context(
                    data.copy(),
                    question.strip(),
                )
                status.update(
                    label="Agent 分析完成",
                    state="complete",
                    expanded=False,
                )

            st.session_state.analysis_answer = answer
            st.session_state.analysis_context = dashboard_context
        except Exception as exc:
            st.error(
                "AI 服务调用失败，请检查 API 配置或网络连接后重试。",
                icon=":material/error:",
            )
            with st.expander("查看错误详情", icon=":material/info:"):
                st.code(str(exc))

context = st.session_state.analysis_context
answer = st.session_state.analysis_answer

if context is not None:
    render_dashboard(context)

if answer:
    render_report(answer)
