import streamlit as st
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(
    page_title="Hackniche",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)

st.title("Home Page")