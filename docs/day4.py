import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows用黑体，系统自带无需安装
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示异常

data = pd.read_excel("财务流水.xls")

expense = data.groupby("类别")["支出"].sum()

print(expense)

expense.plot(
    kind="bar",
    title="Expense Analysis"
)

plt.xlabel("Category")
plt.ylabel("Amount")

plt.savefig("expense_analysis.png")

plt.show()
