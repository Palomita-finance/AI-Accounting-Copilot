import pandas as pd
file_name = input("请输入excel文件名称：")

data = pd.read_excel(file_name)
print(data)
