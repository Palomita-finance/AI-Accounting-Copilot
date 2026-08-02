from src.ai_analyzer import client


def generate_agent_answer(question, context):

    prompt = f"""

你是一名财务分析助手。

用户问题：

{question}


当前分析结果：

财务指标:
{context.metrics}


异常交易:
{context.abnormal}


趋势分析:
{context.trend}


分析建议:
{context.insights}

请根据数据给用户生成专业的财务分析建议。

要求：

1. 使用中文
2. 解释原因
3. 给出建议
"""

    response = client.chat.completions.create(

        model="deepseek-chat",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
