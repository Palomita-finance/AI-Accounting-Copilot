from config import OUTPUT_REPORT


def generate_report(metrics, abnormal_count, insights, ai_result):
    profit_margin = metrics["利润率"]
    profit_margin_text = (
        f"{profit_margin:.2%}"
        if profit_margin is not None
        else "无法计算（无收入）"
    )

    financial_report = f"""财务分析报告
总收入: {metrics["总收入"]}
总支出: {metrics["总支出"]}
利润: {metrics["利润"]}
利润率: {profit_margin_text}
最大支出类别: {metrics["最大支出类别"]}
异常交易数量: {abnormal_count}

分析建议：
{chr(10).join(insights)}

ai分析
{ai_result}
"""

    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write(financial_report)
    print("财务报告已经保存")

    return financial_report
