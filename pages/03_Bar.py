import matplotlib.pyplot as plt
import streamlit as st
import plotly.graph_objects as go
import common
import pandas as pd
import numpy as np
# 시각화
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as ex
import matplotlib
import matplotlib.ticker as ticker
import re

common.page_config()

st.title("Number of Video Games by Genre")

data_2021 = common.get_sales_2021()
data_2021.columns = data_2021.columns.str.strip()
# genre_counts = df['Genre'].value_counts().sort_values(ascending=False)
data_2021.head()
tab1, tab2 = st.tabs(["Pyplot", "Plotly"])

with tab1:
    # plt.bar(genre_counts.index, genre_counts.values)
    # plt.xlabel('Genre')
    # plt.ylabel('Number of Games')
    # plt.title('Number of Video Games by Genre')
    # plt.xticks(rotation=90)
    # st.pyplot(plt)

with tab2:
