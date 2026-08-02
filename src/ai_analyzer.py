import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


def get_api_key():
    """Read the API key from Streamlit Secrets, then fall back to .env."""

    try:
        import streamlit as st

        return st.secrets["DEEPSEEK_API_KEY"]
    except Exception:
        return os.getenv("DEEPSEEK_API_KEY")


class MissingAPIKeyClient:
    @property
    def chat(self):
        raise RuntimeError("Please configure DEEPSEEK_API_KEY")


api_key = get_api_key()
client = (
    OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    if api_key
    else MissingAPIKeyClient()
)


def analyze_with_ai(prompt):

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "你是一名专业财务分析师。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
