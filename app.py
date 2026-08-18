import streamlit as st
from datetime import datetime

from storage import CSV
from analytics import filter_by_date, summarize, format_currency
from charts import build_income_expense_chart


st.set_page_config(page_title="Finance Tracker", layout="wide")

CSV.initialize_csv()

st.title("Finance Tracker")

tab = st.sidebar.radio("Menu", ["Add transaction", "View transactions"])

# ---------------------------------------------------------
# SCREEN 1: Add transaction
# ---------------------------------------------------------
if tab == "Add transaction":
    st.header("New transaction")

    with st.form("new_transaction"):
        date = st.date_input("Date", value=datetime.today())
        amount = st.number_input("Amount", min_value=0.01, step=0.01, format="%.2f")
        category = st.radio("Category", [CSV.INCOME, CSV.EXPENSE], horizontal=True)
        description = st.text_input("Description (optional)")

        submitted = st.form_submit_button("Save")

    if submitted:
        CSV.add_entry(date.strftime(CSV.FORMAT), amount, category, description)
        st.success("Transaction saved successfully!")

# ---------------------------------------------------------
# SCREEN 2: View transactions
# ---------------------------------------------------------
elif tab == "View transactions":
    st.header("Search by period")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date")
    with col2:
        end_date = st.date_input("End date")

    if st.button("Search"):
        df = CSV.load()
        st.session_state["search_result"] = filter_by_date(df, start_date, end_date)

    if "search_result" in st.session_state:
        filtered = st.session_state["search_result"]

        if filtered.empty:
            st.warning("No transactions found in this period.")
        else:
            st.dataframe(
                filtered.sort_values("date").assign(date=lambda d: d["date"].dt.strftime(CSV.FORMAT)),
                use_container_width=True
            )

            summary = summarize(filtered)
            c1, c2, c3 = st.columns(3)
            c1.metric("Total income", format_currency(summary['income']))
            c2.metric("Total expense", format_currency(summary['expense']))
            c3.metric("Balance", format_currency(summary['net']))

            if st.checkbox("Show chart"):
                fig = build_income_expense_chart(filtered)
                st.pyplot(fig)