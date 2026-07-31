import pandas as pd

from src.analyzer import detect_abnormal_expense
from src.chart import create_expense_chart
from src.report import generate_report

data = pd.read_excel("data/financial_data.xls")
result = detect_abnormal_expense(data)


print("发现异常数量", len(result))

expense_summary = data.groupby("类别")["支出"].sum()

create_expense_chart(
    expense_summary.index,
    expense_summary.values
)


total_income = data["收入"].sum()
total_expense = data["支出"].sum()
profit = total_income-total_expense


financial_report = generate_report(
    total_income,
    total_expense,
    profit,
    len(result)
)

print(report)
