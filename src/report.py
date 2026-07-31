def generate_report(metrics, abnormal_count, insights, ai_result):
    report = f"""财务分析报告
总收入: {metrics["总收入"]}
总支出: {metrics["总支出"]}
利润: {metrics["利润"]}
利润率: {metrics["利润率"]:.2%}
最大支出类别: {metrics["最大支出类别"]}
异常交易数量: {abnormal_count}

分析建议：
{chr(10).join(insights)}

ai分析
{ai_result}
"""

    with open("output/financial_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    return report
