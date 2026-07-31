import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, findfont
import matplotlib.font_manager as fm
import os


print("chart.py loaded")


# 自动寻找中文字体
font_path = findfont(
    fm.FontProperties(
        family="Microsoft YaHei"
    )
)

font = FontProperties(
    fname=font_path
)


print("使用字体:", font.get_name())


def create_expense_chart(categories, amounts):

    plt.figure(figsize=(8, 5))

    plt.bar(categories, amounts)

    plt.title(
        "Expense Analysis",
        fontproperties=font
    )

    plt.xlabel(
        "类别",
        fontproperties=font
    )

    plt.ylabel(
        "金额",
        fontproperties=font
    )

    plt.xticks(
        rotation=45,
        fontproperties=font
    )

    plt.tight_layout()

    # 创建输出目录（如果不存在）
    os.makedirs(
        "output",
        exist_ok=True
    )

    plt.savefig(
        "output/expense_chart.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()
