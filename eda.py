import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def eda_st():
    df = pd.read_csv('data/Airline_sa.csv')
    df = df.iloc[:, 1:]
    
    # 페이지 제목
    st.title('항공사 만족도 분석')
    
    # 한글 폰트 지정
    font_path = 'c:/Windows/Fonts/gulim.ttc'  # 한글 폰트 파일의 경로를 지정합니다.
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

    # 각 카테고리별 통계 정보
    if 'show_data2' not in st.session_state:
        st.session_state.show_data2 = False

    show_data2 =  st.button('## 데이터 통계 정보')
    if show_data2:
        st.session_state.show_data2 = not st.session_state.show_data2

    if st.session_state.show_data2:
        st.write(df.describe())

    # 각 카테고리별 시각화
    st.subheader('각 카테고리별 시각화')

    # 성별 분포
    st.write('### 성별 분포')
    gender_fig, ax = plt.subplots()
    sns.countplot(data=df, x='성별', ax=ax)
    st.pyplot(gender_fig)

    # 고객 유형 분포
    st.write('### 고객 유형 분포')
    customer_type_fig, ax = plt.subplots()
    sns.countplot(data=df, x='고객 유형', ax=ax)
    st.pyplot(customer_type_fig)

    # 승객 나이 분포
    st.write('### 승객 나이 분포')
    age_fig, ax = plt.subplots()
    sns.histplot(data=df, x='나이', bins=20, kde=True, ax=ax)
    st.pyplot(age_fig)

    # 승객 비행 목적 분포
    st.write('### 승객 비행 목적 분포')
    travel_type_fig, ax = plt.subplots()
    sns.countplot(data=df, x='비행 목적', ax=ax)
    st.pyplot(travel_type_fig)

    # 비행 클래스 분포
    st.write('### 비행 클래스 분포')
    class_fig, ax = plt.subplots()
    sns.countplot(data=df, x='클래스', ax=ax)
    st.pyplot(class_fig)

    # 비행 거리 분포
    st.write('### 비행 거리 분포')
    flight_distance_fig, ax = plt.subplots()
    sns.histplot(data=df, x='비행 거리', bins=20, kde=True, ax=ax)  # 열 이름 수정
    st.pyplot(flight_distance_fig)

if __name__ == '__main__':
    eda_st()