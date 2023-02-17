import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

with st.container():
    st.write("Popular-Viewed over by 40k times in last week")
    col1, col2, col3 = st.columns(3)
    with col1:
        image = Image.open('Stock.jpg')
        st.image(image, width=180)
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


result = df[df["Risk"] == "HIGH"]
st.write(result)
