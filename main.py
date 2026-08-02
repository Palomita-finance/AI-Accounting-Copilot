import pandas as pd

from src.agent.agent_loop import run_agent


# 读取数据

data = pd.read_excel(
    "data/demo_financial_data.xlsx"
)


# 用户问题

question = """
请分析一下公司的财务风险，
包括异常支出和经营问题。
"""


# 交给Agent

answer = run_agent(
    data,
    question
)


print("\nAI分析结果:")
print(answer)
