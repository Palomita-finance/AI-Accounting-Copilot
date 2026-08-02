import pandas as pd


def load_excel(path):
    """读取 Excel 财务数据并返回 DataFrame。"""

    return pd.read_excel(path)
