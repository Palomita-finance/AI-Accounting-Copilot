import pandas as pd

from src.analyzer import detect_abnormal_expense
from src.chart import create_expense_chart
from src.report import generate_report
from src.metrics import calculate_metrics
from src.insight import generate_insight
from src.ai_prompt import create_financial_prompt
from src.ai_analyzer import analyze_with_ai


data = pd.read_excel("data/financial_data.xls")

metrics = calculate_metrics(data)

result = detect_abnormal_expense(data)

print("发现异常数量", len(result))


expense_summary = data.groupby("类别")["支出"].sum()

create_expense_chart(
    expense_summary.index,
    expense_summary.values
)


insights = generate_insight(metrics, len(result))

prompt = create_financial_prompt(
    metrics,
    insights
)

ai_result = analyze_with_ai(prompt)

financial_report = generate_report(metrics, len(result), insights, ai_result)

print(financial_report)
