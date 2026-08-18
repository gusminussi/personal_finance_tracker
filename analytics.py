import pandas as pd
from storage import CSV
 
 
def filter_by_date(df, start_date, end_date):
    start = (
        pd.to_datetime(start_date, format=CSV.FORMAT)
        if isinstance(start_date, str)
        else pd.to_datetime(start_date)
    )
    end = (
        pd.to_datetime(end_date, format=CSV.FORMAT)
        if isinstance(end_date, str)
        else pd.to_datetime(end_date)
    )
 
    mask = (df["date"] >= start) & (df["date"] <= end)
    return df.loc[mask]
 
 
def summarize(df):
    total_income = df[df["category"] == CSV.INCOME]["amount"].sum()
    total_expense = df[df["category"] == CSV.EXPENSE]["amount"].sum()
    return {
        "income": total_income,
        "expense": total_expense,
        "net": total_income - total_expense
    }
 
 
CURRENCY_SYMBOL = "$"
 
 
def format_currency(value):
    return f"{CURRENCY_SYMBOL} {value:.2f}"
 