import streamlit as st
import calendar
from datetime import datetime

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

incomes = ["Salary","Blog","Other Income"]
expenses = ["Rent", "Utilities","Groceries","Car","Other Expenses","Saving"]
currency = "INR"

years = [datetime.today().year, datetime.today().year+1]
months = list(calendar.month_name[1:])

st.header(f"Add Transaction in {currency}")
with st.form("entry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month: ", months, key="month")
    col2.selectbox("Select Year: ", years, key="year")
    
    "---"
    
    with st.expander("Income"):
        for income in incomes:
            st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
    with st.expander("Expenses"):
        for expense in expenses:
            st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
    with st.expander("Comment"):
        comment = st.text_area("",placeholder="Enter a comment here....")
        
    "---"
    submitted = st.form_submit_button("Save Data")
    if submitted:
        period = str(st.session_state["year"])+"_"+str(st.session_state["month"])
        incomes = {income: st.session_state[income] for income in incomes}
        expenses = {expense: st.session_state[expense] for expense in expenses}
        
        st.write(f"incomes: {incomes}")
        st.write(f"expenses: {expenses}")
        st.success("Data Saved")
    
    st.header("Data Visualization")
    with st.form("saved_periods"):
        period 