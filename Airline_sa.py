import streamlit as st
from corr import corr_st
from eda import eda_st
from home import home_st
from ml import ml_st
from cate import cate_st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io


def main():
    # 아이콘 설정
    # 메뉴 설정

    with st.sidebar:
        st.markdown(
            """
            <div style="font-size: 24px; font-weight: bold; color: skyblue;margin-bottom: 30px;text-align: center;">슬기로운 여행생활!</div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/6350/6350271.png" alt="travel" width="200"/>
        </div>
        """,
        unsafe_allow_html=True
    )


        choice = option_menu("메뉴", ["Home", "EDA 및 데이터 분포", "각 만족도", "상관관계분석","만족도 예측"],
                            icons=['house', 'kanban', 'bi bi-clipboard-data-fill', 'bi bi-clipboard-data','bi bi-robot'],
                            menu_icon="bi bi-airplane-fill", default_index=0,
                            styles={
                                "container": {"padding": "5!important", "background-color": "#fafafa"},
                                "icon": {"color": "black", "font-size": "25px"},
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px",
                                            "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "#80EAFF"},
                            }
                            )


    if choice == 'Home':
        home_st()
    elif choice == 'EDA 및 데이터 분포':
        eda_st()     

    elif choice == '각 만족도':
        selected_column = st.selectbox("카테고리를 선택하세요.", ['기내 와이파이 서비스', '출발/도착 시간 편의성', '온라인 예약 편의성', '탑승구 위치', 
                '음식과 음료', '온라인 탑승', '좌석 편안함', '기내 엔터테인먼트', '탑승 서비스', 
                '다리 공간 서비스','수하물 처리', '체크인 서비스', '기내 서비스', '청결도'])

        if selected_column:
            cate_st(selected_column)
        
    elif choice == '상관관계분석':
        corr_st()

    elif choice == '만족도 예측':
        ml_st()    

if __name__ == '__main__':
    main()