import streamlit as st
import common

common.page_config()
st.title("Data_2021")
st.dataframe(common.get_2021(),
             use_container_width=True,
             hide_index=True)