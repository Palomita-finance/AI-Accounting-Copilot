import pandas as pd
from src.analyzer import detect_abnormal_expense

data = pd.read_excel(input("请输入文件路径："))
result = detect_abnormal_expense(data)

print("发现异常数量", len(result))
