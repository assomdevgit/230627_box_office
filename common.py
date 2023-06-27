import streamlit as st
import pandas as pd

@st.cache_data
def get_sales_2021():
    return pd.read_csv("./KOBIS_2021.csv", encoding="cp949")

def get_sales_2022():
    return pd.read_csv("./KOBIS_2022.csv", encoding="cp949")

def page_config():
    st.set_page_config(
        page_title="Video Game Sales",
        page_icon="🎮",
    )