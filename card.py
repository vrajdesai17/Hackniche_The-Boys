import streamlit as st
import pandas as pd
from PIL import Image

# st.set_page_config(
#     page_title="Hackniche",
#     page_icon="chart_with_upwards_trend",
#     layout="wide",
# )


with st.container():
    st.write("Popular-Viewed over by 40k times in last week")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('Stock.jpg')
        st.image(image, width=300)
    with col2:
        st.write("Equity & Gold")
        st.write(
            "Create wealth with equities,stay protected with Gold. The sweet spot")
        with st.container():
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Min.Amount")
                st.write("$292")
            with col5:
                st.write("4Y CAGR")
                st.write("15.29%")
            with col6:
                st.write("Low Volatility")


with st.container():
    st.write("Popular-Viewed over by 40k times in last week")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('Stock.jpg')
        st.image(image, width=300)
    with col2:
        st.write("Equity & Gold")
        st.write(
            "Create wealth with equities,stay protected with Gold. The sweet spot")
        with st.container():
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Min.Amount")
                st.write("$292")
            with col5:
                st.write("4Y CAGR")
                st.write("15.29%")
            with col6:
                st.write("Medium Volatility")

with st.container():
    st.write("Popular-Viewed over by 40k times in last week")
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open('Stock.jpg')
        st.image(image, width=300)
    with col2:
        st.write("Equity & Gold")
        st.write(
            "Create wealth with equities,stay protected with Gold. The sweet spot")
        with st.container():
            col4, col5, col6 = st.columns(3)
            with col4:
                st.write("Min.Amount")
                st.write("$292")
            with col5:
                st.write("4Y CAGR")
                st.write("15.29%")
            with col6:
                st.write("High Volatility")


# with st.container():
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         with st.container():
#             st.write("Popular-Viewed over by 40k times in last week")
#             col4, col5 = st.columns(2)
#             with col4:
#                 image = Image.open('Stock.jpg')
#                 st.image(image, width=120)
#             with col5:
#                 st.write("Equity & Gold")
#                 st.write(
#                     "Create wealth with equities,stay protected with Gold. The sweet spot")
#                 with st.container():
#                     col6, col7, col8 = st.columns(3)
#                     with col6:
#                         st.write("Min.Amount")
#                         st.write("$292")
#                     with col7:
#                         st.write("4Y CAGR")
#                         st.write("15.29%")
#                     with col8:
#                         st.write("Low Volatility")
