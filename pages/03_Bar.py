import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import common


common.page_config()

st.title("2021 Top 10")

df = common.get_2021()

# genre_counts = df['Genre'].value_counts().sort_values(ascending=False)

tab1, tab2 = st.tabs(["Sales", "Numbers"])

with tab1:
    data = {
        'category': ['A', 'B', 'C', 'D', 'E'],
        'value': [10, 20, 15, 25, 30]
    }

    # 데이터를 DataFrame으로 변환
    df = pd.DataFrame(data)

    # category로 그룹화하여 그룹별 합계 계산
    # value 값 변경
    for i in range(len(df['category'])):
        if df['category'][i] != "A":
            df['category'][i] = "F"

    df1 = df.groupby('category')['value'].sum()
    df1.head()

    # 막대 그래프 그리기
    categories = df1.index
    values = df1.values

    plt.bar(categories, values)
    st.pyplot(plt)

with tab2:
    data = {
        'category': ['A', 'B', 'C', 'D', 'E'],
        'value': [10, 20, 15, 25, 30]
    }

    # 데이터를 DataFrame으로 변환
    df = pd.DataFrame(data)

    # category로 그룹화하여 그룹별 합계 계산
    # value 값 변경
    for i in range(len(df['category'])):
        if df['category'][i] != "A":
            df['category'][i] = "F"

    df1 = df.groupby('category')['value'].sum()
    df1.head()

    # 막대 그래프 그리기
    categories = df1.index
    values = df1.values

    plt.bar(categories, values)
    st.pyplot(plt)