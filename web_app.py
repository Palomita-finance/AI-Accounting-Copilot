import streamlit as st

from src.agent.agent_loop import run_agent
from src.data_loader import load_excel


REQUIRED_COLUMNS = {"日期", "摘要", "类别", "收入", "支出"}


st.set_page_config(
    page_title="AI Accounting Copilot",
    page_icon="📊",
    layout="centered"
)

st.title("AI Accounting Copilot")
st.caption("Upload financial data and let the LLM Agent orchestrate the analysis tools.")

uploaded_file = st.file_uploader(
    "上传 Excel 财务数据",
    type=["xlsx", "xls"],
    help="Excel 字段要求：日期 | 摘要 | 类别 | 收入 | 支出"
)

question = st.text_input(
    "分析问题",
    value="请分析公司的财务风险和经营问题"
)

if st.button("开始分析", type="primary"):
    if uploaded_file is None:
        st.warning("请先上传 Excel 文件。")
    elif not question.strip():
        st.warning("请输入需要分析的问题。")
    else:
        try:
            data = load_excel(uploaded_file)
            missing_columns = REQUIRED_COLUMNS - set(data.columns)

            if missing_columns:
                missing_text = "、".join(sorted(missing_columns))
                st.error(f"Excel 缺少必要字段：{missing_text}")
            else:
                with st.spinner("Agent 正在分析财务数据..."):
                    answer = run_agent(data, question.strip())

                st.subheader("AI 财务分析报告")
                st.markdown(answer)
        except Exception as exc:
            st.error(f"分析失败：{exc}")
