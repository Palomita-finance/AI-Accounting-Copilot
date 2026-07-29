def detect_abnormal_expense(data):
    abnormal = []
    for index, row in data.iterrows():
        if row["支出"] > 1000:
            abnormal.append(row)
    return abnormal
