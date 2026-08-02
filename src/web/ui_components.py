import streamlit as st


REQUIRED_COLUMNS = {"日期", "摘要", "类别", "收入", "支出"}


def render_sidebar():
    with st.sidebar:
        st.header("AI Accounting Copilot")
        st.caption("智能财务分析助手")
        st.markdown(
            "将 LLM 工具调度与确定性财务分析结合，生成结构化经营诊断。"
        )
        st.badge("Version v2.2", icon=":material/new_releases:", color="blue")
        st.subheader("Architecture")
        st.write("LLM Agent + Financial Tools")
        st.subheader("Tech stack")
        st.markdown("Python  ·  Pandas  ·  DeepSeek  ·  Streamlit")


def render_header():
    with st.container(border=True):
        st.title("AI Accounting Copilot")
        st.markdown("**智能财务分析助手**")
        st.caption("AI-powered Financial Analysis Agent")


def render_file_summary(uploaded_file, data, missing_columns, file_error):
    if uploaded_file is None:
        st.caption("支持 XLSX、XLS；必需字段：日期、摘要、类别、收入、支出")
        return

    if file_error is not None:
        st.error(
            "❌ Excel格式错误，请检查文件内容。",
            icon=":material/error:",
        )
        return

    if missing_columns:
        st.error("❌ Excel格式错误，请检查字段。", icon=":material/error:")
        st.markdown("**缺少字段：**")
        for column in sorted(missing_columns):
            st.markdown(f"- `{column}`")
        return

    st.success("文件加载成功", icon=":material/check_circle:")
    file_info = st.container(horizontal=True)
    with file_info:
        st.markdown(f"**文件名称**  `{uploaded_file.name}`")
        st.markdown(f"**数据行数**  {len(data):,} transactions detected")
        st.markdown("**字段检查**  ✓ Passed")
