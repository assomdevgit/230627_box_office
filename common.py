import streamlit as st
import pandas as pd

@st.cache_data
def get_sales():
    return pd.read_csv("./KOBIS_2022.csv", encoding="utf-8")

def page_config():
    st.set_page_config(
        page_title="Video Game Sales",
        page_icon="🎮",
    )