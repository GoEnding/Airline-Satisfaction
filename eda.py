import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def eda_st():
    plt.rcParams['axes.unicode_minus'] = False
    if platform.system() == 'Linux':
        rc('font', family='NanumGothic')
    df = pd.read_csv('data/Airline_sa.csv')
    df = df.iloc[:, 1:]
    
    # 페이지 제목
    st.title('항공사 만족도 분석')
    
    # 한글 폰트 지정

    tab1, tab2= st.tabs(['EDA' , '데이터 분포']) 
        # 데이터 출력을 위한 토글 버튼
    with tab1:

        new_data = ['데이터 미리보기','데이터 통계치']
        dataset = st.radio('데이터 선택',new_data)
        
        if dataset == new_data[0]:
            st.info('와이파이서비스부터 청결도까지는 점수 0~5로 나타내고,0:불만족 5:만족을 보여줍니다')
            st.dataframe(df)
        elif dataset == new_data[1]:
            st.dataframe(df.describe())



        st.text('보고싶은 열을 선택하면, 해당 열의 최대/최소 데이터를 보여드립니다.')
        column_list = ['나이','비행 거리','출발 지연(분)','도착 지연(분)']
        choice_column = st.selectbox('컬럼을 선택하세요.',column_list)

        st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')
        st.dataframe(df.loc[df[choice_column] == df[choice_column].max(),])

        st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')
        st.dataframe(df.loc[df[choice_column] == df[choice_column].min(),])



        # 각 카테고리별 시각화

        with tab2:
            plt.rcParams['axes.unicode_minus'] = False
            if platform.system() == 'Linux':
                rc('font', family='NanumGothic')

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