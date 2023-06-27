import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import common
import pandas as pd


common.page_config()

st.title("2021 Top 10")

data_2021 = common.get_2021()
data_2022 = common.get_2021()

common.get_preprocessing(data_2021, data_2022)

# data_2021.columns = data_2021.columns.str.strip()
# data_2022.columns = data_2022.columns.str.strip()
# # genre_counts = df['Genre'].value_counts().sort_values(ascending=False)
# null_list = ['대표국적', '국적', '개봉일', '제작사', '배급사', '등급', '장르', '감독', '배우']
# for i in null_list:
#     data_2021[i] = data_2021[i].fillna('정보없음')
# null_list = ['대표국적', '국적', '개봉일', '제작사', '배급사', '등급', '장르', '감독', '배우']
# for i in null_list:
#     data_2022[i] = data_2022[i].fillna('정보없음')
#
# data_2021['장르'] = data_2021['장르'].apply(lambda x: x.split(',')[0])
# data_2022['장르'] = data_2022['장르'].apply(lambda x: x.split(',')[0])
# data_2021.rename(columns={'장르':'대표장르'}, inplace=True)
# data_2022.rename(columns={'장르':'대표장르'}, inplace=True)
# def numbering(x): # 인트 변환 함수
#     return int(x.replace(',',''))
#
# number_list = ['매출액', '누적매출액', '관객수', '누적관객수', '스크린수'] #인트 변환 적용
# for i in number_list:
#     data_2021[i] = data_2021[i].apply(numbering)
# number_list = ['매출액', '누적매출액', '관객수', '누적관객수', '스크린수'] #인트 변환 적용
# for i in number_list:
#     data_2022[i] = data_2022[i].apply(numbering)
#
df_2021 = data_2021[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
df_2022 = data_2022[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
df_2021.head()

sale_grp_2021 = df_2021.groupby('대표국적')['매출액'].sum().nlargest(20)
sale_grp_2022 = df_2022.groupby('대표국적')['매출액'].sum().nlargest(20)
sale_grp_2021

tab1, tab2 = st.tabs(["Sales", "Numbers"])

with tab1:
    # 데이터 생성

    # 막대 그래프 크기 조절
    plt.figure(figsize=(12, 4))
    plt.xlabel('국가')
    plt.ylabel('매출(단위 억원)')
    plt.title('국가별 매출 성장률')

    # 막대 너비 설정
    bar_width = 0.5

    # 첫 번째 데이터 그리기
    plt.bar(sale_grp_2021.index, sale_grp_2021.values // 100_000_000, width=bar_width, align='center', label='2021')

    # 두 번째 데이터 겹쳐서 그리기
    plt.bar(sale_grp_2022.index, sale_grp_2022.values // 100_000_000, width=bar_width, align='edge', label='2022')

    # 범례(legend) 표시
    plt.legend()

    # x축 레이블 기울기 설정
    plt.xticks(rotation=90)

    st.pyplot(plt)


with tab2:

    top10_2021 = df_2021.iloc[:10, :]
    top10_2022 = df_2022.iloc[:10, :]
    # 데이터 설정
    x = ['1위', '2위', '3위', '4위', '5위', '6위', '7위', '8위', '9위', '10위']  # x축 레이블
    y1 = top10_2021.loc[:, '관객수']  # 첫 번째 막대 그래프 데이터
    y2 = top10_2022.loc[:, '관객수']  # 두 번째 막대 그래프 데이터

    # 첫 번째 막대 그래프 생성
    trace1 = go.Bar(
        x=x,
        y=y1,
        name='2021'
    )

    # 두 번째 막대 그래프 생성
    trace2 = go.Bar(
        x=x,
        y=y2,
        name='2022'
    )

    # 데이터를 리스트로 묶고 레이아웃 설정
    data = [trace1, trace2]
    layout = go.Layout(
        barmode='group'  # 그룹 형태로 막대 그래프를 그리도록 설정
    )

    # 그래프 생성
    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(
        title={
            'text': "21년 22년 탑 10 관객수 비교",
            'x': 0.5,  # 제목을 표 가운데로 위치시키기 위해 x 값 조정 (0.0 ~ 1.0)
            'xanchor': 'center',  # x 축 기준으로 제목을 가운데 정렬
            'yanchor': 'top'  # 제목을 상단에 위치
        })

    st.pyplot(plt)