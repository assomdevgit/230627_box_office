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
data_2022 = common.get_2022()

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
    st.subheader("국가별 매출 현황")
    # 데이터 생성
    trace1 = go.Bar(x=sale_grp_2021.index, y=sale_grp_2021.values, name='2021')
    trace2 = go.Bar(x=sale_grp_2022.index, y=sale_grp_2022.values, name='2022')

    data = [trace1, trace2]

    layout = go.Layout(xaxis={'title': '국가별'}, yaxis={'title': '매출액'})

    fig = go.Figure(data=data, layout=layout)

    fig.update_layout(
        title={
            'text': "21년 22년 국가별 매출",
            'x': 0.5,  # 제목을 표 가운데로 위치시키기 위해 x 값 조정 (0.0 ~ 1.0)
            'xanchor': 'center',  # x 축 기준으로 제목을 가운데 정렬
            'yanchor': 'top'  # 제목을 상단에 위치
        })
    # st.pyplot(plt)
    st.plotly_chart(fig)

    st.write()
    st.subheader("장르별 영화 상영수")

    gnr_repl_20021 = df_2021['대표장르']
    gnr_grp_2021 = gnr_repl_20021.groupby(gnr_repl_20021.values).count()

    gnr_repl_20022 = df_2022['대표장르']
    gnr_grp_2022 = gnr_repl_20022.groupby(gnr_repl_20022.values).count()

    trace1 = go.Bar(x=gnr_grp_2021.index, y=gnr_grp_2021.values, name='2021')
    trace2 = go.Bar(x=gnr_grp_2022.index, y=gnr_grp_2022.values, name='2022')

    data = [trace1, trace2]

    layout = go.Layout(xaxis={'title': '장르'}, yaxis={'title': '상영수'})

    fig = go.Figure(data=data, layout=layout)

    fig.update_layout(
        title={
            'text': "21년 22년 장르별 상영수",
            'x': 0.5,  # 제목을 표 가운데로 위치시키기 위해 x 값 조정 (0.0 ~ 1.0)
            'xanchor': 'center',  # x 축 기준으로 제목을 가운데 정렬
            'yanchor': 'top'  # 제목을 상단에 위치
        })

    st.plotly_chart(fig)

    st.write()
    st.subheader("국가별 영화 관객수")

    # 국가별 10만 이상의 관객수
    top_2021 = df_2021[df_2021['관객수'] > 100_000]
    grp_audi_2021 = top_2021.groupby('대표국적')['관객수'].sum()

    top_2022 = df_2022[df_2021['관객수'] > 100_000]
    grp_audi_2022 = top_2022.groupby('대표국적')['관객수'].sum()

    data = [go.Pie(labels=grp_audi_2021.index, values=grp_audi_2021.values)]
    layout = go.Layout(title='2021년 국가별 영화 관객수')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)

    data = [go.Pie(labels=grp_audi_2022.index, values=grp_audi_2022.values)]
    layout = go.Layout(title='2022년 국가별 영화 관객수')
    fig = go.Figure(data=data, layout=layout)
    st.plotly_chart(fig)


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
    # 그래프 출력
    fig.show()
    # st.pyplot(fig)
    st.plotly_chart(fig)