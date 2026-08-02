def generate_insight(metrics, abnormal_count):

    insights = []

    # 利润率分析
    if metrics["利润率"] is None:

        insights.append(
            "当前没有收入数据，无法计算利润率，需要关注收入来源和经营状态"
        )

    elif metrics["利润率"] < 0.3:

        insights.append(
            "当前利润率较低，需要关注成本控制和盈利能力提升"
        )

    else:

        insights.append(
            "当前利润率较高，盈利状况较好"
        )

    # 最大支出类别分析
    insights.append(
        f"最大支出类别为{metrics['最大支出类别']}，建议对该类别的支出进行优化"
    )

    # 异常交易分析
    if abnormal_count > 0:

        insights.append(
            f"发现{abnormal_count}笔异常交易，请及时核查"
        )

    else:

        insights.append(
            "未发现明显异常交易"
        )

    return insights
