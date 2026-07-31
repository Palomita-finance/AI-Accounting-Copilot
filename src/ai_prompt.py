def create_financial_prompt(metrics, insights):
    prompt = f"""
    你是一名专业财务分析师。
    请根据以下财务数据生成分析建议：

财务指标:
总收入: {metrics["总收入"]}
总支出: {metrics["总支出"]}
利润: {metrics["利润"]}
利润率: {metrics["利润率"]:.2%}
最大支出类别: {metrics["最大支出类别"]}
已有建议
\n{chr(10).join(insights)}
请输出：
1. 财务状况总结
2. 风险点
3. 改进建议

"""
    return prompt
