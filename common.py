import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns


def get_2022():
    data_2022 = pd.read_csv("./KOBIS_2021.csv", encoding="cp949")
    return data_2022

def get_2021():
    data_2021 = pd.read_csv("./KOBIS_2022.csv", encoding="cp949")
    return data_2021

def page_config():
    st.set_page_config(
        page_title="movie"
    )

def get_preprocessing(data_2021, data_2022):
    data_2021.columns = data_2021.columns.str.strip()
    data_2022.columns = data_2022.columns.str.strip()
    # genre_counts = df['Genre'].value_counts().sort_values(ascending=False)
    null_list = ['대표국적', '국적', '개봉일', '제작사', '배급사', '등급', '장르', '감독', '배우']
    for i in null_list:
        data_2021[i] = data_2021[i].fillna('정보없음')
    null_list = ['대표국적', '국적', '개봉일', '제작사', '배급사', '등급', '장르', '감독', '배우']
    for i in null_list:
        data_2022[i] = data_2022[i].fillna('정보없음')

    data_2021['장르'] = data_2021['장르'].apply(lambda x: x.split(',')[0])
    data_2022['장르'] = data_2022['장르'].apply(lambda x: x.split(',')[0])
    data_2021.rename(columns={'장르':'대표장르'}, inplace=True)
    data_2022.rename(columns={'장르':'대표장르'}, inplace=True)
    # def numbering(x): # 인트 변환 함수
    #     return int(x.replace(',',''))

    number_list = ['매출액', '누적매출액', '관객수', '누적관객수', '스크린수'] #인트 변환 적용
    for i in number_list:
        data_2021[i] = data_2021[i].apply(numbering)
    number_list = ['매출액', '누적매출액', '관객수', '누적관객수', '스크린수'] #인트 변환 적용
    for i in number_list:
        data_2022[i] = data_2022[i].apply(numbering)

    # df_2021 = data_2021[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
    # df_2022 = data_2022[['영화명', '개봉일', '매출액', '매출액점유율', '누적매출액', '관객수', '누적관객수', '스크린수', '대표국적', '등급', '대표장르']]
    # df_2021.head()

def numbering(x): # 인트 변환 함수
    return int(x.replace(',',''))