import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Hackniche",
    page_icon="chart_with_upwards_trend",
    layout="wide",
)

with st.container():
    st.write("Popular-Viewed over by 40k times in last week")
    col1, col2, col3 = st.columns(3)
    with col1:
        image = Image.open('Stock.jpg')
        st.image(image, width=300)
    with col2:
        st.write("Equity & Gold")
        st.write("Managed by WindMill Capital")
        st.write(
            "Create wealth with equities,stay protected with Gold. The sweet spot")
        with col3:
            st.write("4Y CAGR")
            st.write("15.29%")
            st.write("Low Volatility")


data = pd.read_csv("Ide.csv")
df = pd.DataFrame(data)


result = df[df["Risk"] == "LOW"]
st.write(result)

with st.container():
    st.write("Overview")
    col1, col2 = st.columns(2)

    with col1:
        st.write("About the smallcase")
        st.write(
            "This smallcase invests in Equity & Gold, fixing their weights to 70% and 30%")
        st.write(
            "smallcase invests in large-cap companies using Nippon India ETF Nifty Bees")

    with col2:
        st.write("Blog Posst")
        st.write("Read more about Equity & gold")
        st.write("Methodology")
        st.write("Know how this smallcase was created")
        st.write("Factsheet")
        st.write("Download key points of this smallcase")
