import streamlit as st
import common

common.page_config()
st.title("Data_2022")
st.dataframe(common.get_sales_2022(),
             use_container_width=True,
             hide_index=True)