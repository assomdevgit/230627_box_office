import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import common


common.page_config()

st.title("2021 Top 10")

data_2021 = common.get_2021()
data_2022 = common.get_2021()

data_2021.columns = data_2021.columns.str.strip()
data_2022.columns = data_2022.columns.str.strip()
# genre_counts = df['Genre'].value_counts().sort_values(ascending=False)
null_list = ['대표국적', '국적', '개봉일', '제작사', '배급사', '등급', '장르', '감독', '배우']
for i in null_list:
    data_2021[i] = data_2021[i].fillna('정보없음')
null_list = ['대표국적', '국적', '개봉일', '제작사', '배급사', '등급', '장르', '감독', '배우']
for i in null_list:
    data_2022[i] = data_2022[i].fillna('정보없음')

def numbering(x): # 인트 변환 함수
    return int(x.replace(',',''))

number_list = ['매출액', '누적매출액', '관객수', '누적관객수', '스크린수'] #인트 변환 적용
for i in number_list:
    data_2021[i] = data_2021[i].apply(numbering)
number_list = ['매출액', '누적매출액', '관객수', '누적관객수', '스크린수'] #인트 변환 적용
for i in number_list:
    data_2022[i] = data_2022[i].apply(numbering)

df_2021 = data_2021[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
df_2022 = data_2022[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
df_2021.head()
tab1, tab2 = st.tabs(["Sales", "Numbers"])

with tab1:

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