import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

# SessionState 클래스 정의
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

# 현재 세션의 고유 ID를 얻는 함수
def get_session_id():
    session_id = get_report_ctx().session_id
    session_info = Server.get_current()._get_session_info(session_id)
    return session_info.id

# SessionState 생성
session_state = SessionState(button_clicked=False)

# 버튼 생성
if st.button("페이지 이동"):
    session_state.button_clicked = True

# 버튼이 클릭되었을 때 처리
if session_state.button_clicked:
    # 페이지 이동을 위해 쿼리 매개변수 설정
    query_params = {"page": "new_page"}
    new_url = st.experimental_set_query_params(**query_params)

    # 페이지 리다이렉션
    st.experimental_rerun()