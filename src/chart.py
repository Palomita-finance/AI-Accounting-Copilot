import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# 指定中文字体（Windows微软雅黑）
font = FontProperties(
    fname=r"C:\Windows\Fonts\msyh.ttc"
)


def create_expense_chart(categories, amounts):
    """
    创建支出分析柱状图

    输入：
    categories: 支出类别列表
    amounts: 每个类别对应的支出金额列表

    输出：
    在output文件夹生成expense_chart.png
    """

    # 设置图片大小
    plt.figure(figsize=(8, 5))

    # 绘制柱状图
    plt.bar(categories, amounts)

    # 标题
    plt.title(
        "Expense Analysis",
        fontproperties=font
    )

    # x轴名称
    plt.xlabel(
        "类别",
        fontproperties=font
    )

    # y轴名称
    plt.ylabel(
        "金额",
        fontproperties=font
    )

    # x轴文字旋转45度，防止类别太长重叠
    plt.xticks(
        rotation=45,
        fontproperties=font
    )

    # 自动调整布局，避免文字被截断
    plt.tight_layout()

    # 保存图片
    plt.savefig(
        "output/expense_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    # 关闭图片对象，释放资源
    plt.close()
