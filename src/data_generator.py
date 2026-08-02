import pandas as pd
import random
from datetime import datetime, timedelta


def generate_financial_data(rows=200):

    categories = [
        "办公用品",
        "差旅",
        "餐饮",
        "设备采购",
        "工资",
        "软件服务"
    ]

    summaries = [
        "采购办公用品",
        "员工出差",
        "客户招待",
        "购买设备",
        "工资发放",
        "软件订阅"
    ]

    data = []

    start_date = datetime(2026, 1, 1)

    for i in range(rows):

        date = (
            start_date
            + timedelta(
                days=random.randint(0, 180)
            )
        )

        category = random.choice(categories)

        summary = random.choice(summaries)

        # 大部分正常支出
        expense = random.randint(
            100,
            3000
        )

        # 制造少量异常大额支出
        if random.random() < 0.05:
            expense = random.randint(
                5000,
                20000
            )

        income = 0

        data.append(
            [
                date.strftime("%Y-%m-%d"),
                summary,
                category,
                income,
                expense
            ]
        )

    df = pd.DataFrame(
        data,
        columns=[
            "日期",
            "摘要",
            "类别",
            "收入",
            "支出"
        ]
    )

    return df
