def calculate_metrics(data):

    total_income = data["收入"].sum()
    total_expense = data["支出"].sum()
    profit = total_income - total_expense
    profit_margin = profit / total_income if total_income != 0 else None
    expense_by_category = data.groupby("类别")["支出"].sum()
    max_expense_category = (
        expense_by_category.idxmax()
        if not expense_by_category.empty
        else None
    )

    metrics = {
        "总收入": total_income,
        "总支出": total_expense,
        "利润": profit,
        "利润率": profit_margin,
        "最大支出类别": max_expense_category
    }
    return metrics
