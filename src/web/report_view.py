import streamlit as st


def render_report(answer):
    with st.container(border=True):
        st.markdown("## Financial diagnosis")
        st.markdown(answer)
        st.download_button(
            "Download report",
            data=answer,
            file_name="financial_report.md",
            mime="text/markdown",
            icon=":material/download:",
            on_click="ignore",
            width="stretch",
        )
