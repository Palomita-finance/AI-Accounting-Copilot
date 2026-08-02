from src.data_generator import generate_financial_data


data = generate_financial_data(300)


data.to_excel(
    "data/demo_financial_data.xlsx",
    index=False
)


print("模拟财务数据生成完成")
