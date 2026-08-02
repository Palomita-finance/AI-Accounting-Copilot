import pandas as pd


def analyze_trend(data):

    data["日期"] = pd.to_datetime(
        data["日期"]
    )

    monthly_expense = (
        data
        .groupby(
            data["日期"].dt.month
        )["支出"]
        .sum()
    )

    return monthly_expense
