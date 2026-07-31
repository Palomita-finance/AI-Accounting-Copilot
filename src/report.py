def generate_report(total_income, total_expense, profit, abnormal_count):
    report = f"""财务分析报告
总收入: {total_income}
总支出: {total_expense}
利润: {profit}
异常交易数量: {abnormal_count}
"""

    with open("output/financial_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    return report
