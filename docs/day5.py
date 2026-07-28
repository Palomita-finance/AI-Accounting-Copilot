import pandas as pd

data = pd.read_excel("财务流水.xls")

total_income = data["收入"].sum()
total_expense = data["支出"].sum()
profit = total_income-total_expense

expense_category = data.groupby("类别")["支出"].sum()
max_expense = expense_category.idxmax()
max_amount = expense_category.max()

report = f"""
财务分析报告
总收入：{total_income}元
总支出：{total_expense}元
利润：{profit}元
最大支出类别：{max_expense},金额：{max_amount}元
"""

with open("财务分析报告.txt", "w", encoding="utf-8") as f:
    f.write(report)
