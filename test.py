import streamlit as st

# Define the sidebar menu
menu = ["Home", "About", "Contact"]
choice = st.sidebar.selectbox("Select a page", menu)

# Render the chosen page
if choice == "Home":
    st.write("Welcome to the home page!")
elif choice == "About":
    st.write("This is the about page.")
else:
    st.write("Get in touch with us on the contact page.")
