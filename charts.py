import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from storage import CSV
 
 
def build_income_expense_chart(df):
    plot_df = df.set_index("date")
 
    income_daily = plot_df[plot_df["category"] == CSV.INCOME]["amount"].resample("D").sum().fillna(0)
    expense_daily = plot_df[plot_df["category"] == CSV.EXPENSE]["amount"].resample("D").sum().fillna(0)
 
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(income_daily.index, income_daily.values, label="Income", color="g", width=0.3, align="edge")
    ax.bar(expense_daily.index, expense_daily.values, label="Expense", color="r", width=-0.3, align="edge")
 
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
 
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.set_title("Revenues and expenses over time")
    ax.legend()
    ax.grid(True, axis="y")
    fig.tight_layout()
 
    return fig