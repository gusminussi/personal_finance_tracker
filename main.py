import matplotlib.pyplot as plt
 
from storage import CSV
from analytics import filter_by_date, summarize, format_currency
from charts import build_income_expense_chart
from data_entry import get_amount, get_category, get_date, get_description
 
 
def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or enter for today's date: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("Entry added successfully!")
 
 
def view():
    start_date = get_date("Enter the start date (dd-mm-yyyy): ")
    end_date = get_date("Enter the end date (dd-mm-yyyy): ")
 
    df = CSV.load()
    filtered_df = filter_by_date(df, start_date, end_date)
 
    if filtered_df.empty:
        print("No transactions found in the given date range.")
        return
 
    print(f"Transactions from {start_date} to {end_date}")
    print(
        filtered_df.to_string(
            index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
        )
    )
 
    summary = summarize(filtered_df)
    print("\nSummary: ")
    print(f"Total Income: {format_currency(summary['income'])}")
    print(f"Total Expense: {format_currency(summary['expense'])}")
    print(f"Net Savings: {format_currency(summary['net'])}")
 
    if input("Do you want to see a plot? (y/n) ").lower() == "y":
        build_income_expense_chart(filtered_df)
        plt.show()
 
 
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
 
        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")
 
 
if __name__ == "__main__":
    main()