from config import ABNORMAL_THRESHOLD


def detect_abnormal_expense(data):

    abnormal = data[
        data["支出"] > ABNORMAL_THRESHOLD
    ]

    return abnormal
