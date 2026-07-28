import pandas as pd

file_name = input("请输入excel名称：")
data = pd.read_excel(file_name)

# 如果直接in data的话，只能得到表头列名，再加上iterrows才能遍历每一行
# index是索引，表示第几行，index=0就是第一行
# row表示一整行数据，row["支出"]表示该行对应支出的数据

abnormal = []

for index, row in data.iterrows():
    if row["支出"] > 1000:
        abnormal.append(row)

print(abnormal)
print("共发现", len(abnormal), "条异常支出")
