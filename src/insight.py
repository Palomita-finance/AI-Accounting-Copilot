def generate_insight(metrics, abnormal_count):
    insights = []
    if metrics["利润率"] < 0.3:
        insights.append("当前利润率较高，盈利状况良好")
    else:
        insights.append("当前利润率较低，需要关注成本控制")
    insights.append(f"最大支出类别为{metrics['最大支出类别']}，建议对该类别的支出进行优化")
    if abnormal_count > 0:
        insights.append(f"发现{abnormal_count}笔异常交易，请及时核查")
    else:
        insights.append("未发现明显异常")
    return insights
