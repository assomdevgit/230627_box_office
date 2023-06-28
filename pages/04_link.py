import streamlit as st

# 이미지 파일 경로
image_path = "img/아바타.jpg"

# 이미지를 클릭했을 때 처리
if st.button("이미지 보기"):
    # 이미지 표시
    st.image(image_path, caption="클릭해서 이미지를 보세요")