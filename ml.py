import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

import sklearn
from sklearn.preprocessing import LabelEncoder
import platform
from PIL import Image



def ml_st():
    plt.rcParams['axes.unicode_minus'] = False
    if platform.system() == 'Linux':
        rc('font', family='NanumGothic')
    elif platform.system() == 'Windows':
        # 윈도우 환경에서 한글 폰트 설정
        font_path = "c:\WINDOWS\Fonts\GULIM.TTC"  # 한글 폰트 파일 경로
        font_name = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font_name)    
    st.title('당신의 비행은 만족스러웠나요?')
    # 1. 예측하기 위해서 유저한테 입력받는다.
    st.text('성별을 선택하세요.')
    gender = st.radio('성별 선택', ['남자','여자'])
    if gender =='남자' :
        gender = 1
    elif gender == '여자' :
        gender = 0

    st.text('고객 유형은 무엇인가요?')
    customer_type = st.radio('고객 유형',['Loyal Customer','disLoyal Customer'])
    if customer_type == 'Loyal Customer':
        customer_type = 1
    elif customer_type == 'disLoyal Customer':
        customer_type = 0
    
    st.text('나이를 입력해주세요')
    age = st.number_input('나이 입력', min_value=0, max_value=100, value= 24)

    st.text('비행목적은 무엇인가요?')
    travel_type = st.radio('목적 선택',['Business travel','Personal Travel'])
    if travel_type == 'Business travel':
        travel_type = 0
    elif travel_type == 'Personal Travel':
        travel_type = 1

    st.text('비행 클래스는 무엇인가요?')
    flight_class = st.radio('클래스 선택',['Business','Eco','Eco Plus'])

    st.text('비행 거리는 얼마나 되나요?')
    flight_dis = st.number_input('비행거리 입력', min_value=0, max_value=100000, value= 500)

    st.text('출발 지연(분)은 얼마나 되셨나요?')
    start_delay = st.number_input('출발 지연(분)', min_value=0, max_value=1600, value= 0,step=10)

    st.text('도착 지연(분)은 얼마나 되셨나요?')
    arrive_delay = st.number_input('도착 지연(분)', min_value=0, max_value=1600, value= 0,step=10)


    st.text('온라인 탑승에 대한 만족도는 어땠나요?')
    sat1 = st.select_slider('만족도(0점:불만족,5점:만족)', [0, 1, 2, 3, 4, 5], key='online_boarding')

    st.text('좌석 편안함에 대한 만족도는 어땠나요?')
    sat2 = st.select_slider('만족도(0점:불만족,5점:만족)', [0, 1, 2, 3, 4, 5], key='seat_comfort')

    st.text('기내 엔터테인먼트에 대한 만족도는 어땠나요?')
    sat3 = st.select_slider('만족도(0점:불만족,5점:만족)', [0, 1, 2, 3, 4, 5], key='entertainment')

    st.text('탑승 서비스에 대한 만족도는 어땠나요?')
    sat4 = st.select_slider('만족도(0점:불만족,5점:만족)', [0, 1, 2, 3, 4, 5], key='boarding_service')

    st.text('다리 공간 서비스에 대한 만족도는 어땠나요?')
    sat5 = st.select_slider('만족도(0점:불만족,5점:만족)', [0, 1, 2, 3, 4, 5], key='legroom_service')


    if st.button('예측 및 상관관계 분석'):
        ct = joblib.load('ct_Air.pkl')
        print(ct)
        df = pd.read_csv('df_Air.csv')
        print(df)
        classifier= joblib.load('classifier_Air.pkl')
        print(classifier)
        df = df.iloc[:, 1:]
        new_data = [gender, customer_type, age, travel_type, flight_class, flight_dis, start_delay, arrive_delay, sat1, sat2, sat3, sat4, sat5]
        print(new_data)
        new_data = np.array(new_data).reshape(1,-1)
        print(new_data)
        new_data_trans = ct.transform(new_data)
        print(new_data_trans)
        sati_pre = classifier.predict(new_data_trans)
        print(sati_pre)
        if sati_pre == 1:
            st.write('### 만족스러운 여행이셨군요!!')
            img = Image.open('data/woman_travel.png')
    
            st.image(img)
            
            # 만족일 경우에만 상관관계 분석 수행
            label_encoder = LabelEncoder()
            df['만족도'] = label_encoder.fit_transform(df['만족도'])  # 만족도 레이블 인코딩

            # 선택된 특성과 만족도 컬럼 간의 상관관계 계산
            correlations = []
            for feature in df.columns[:-1]:
                if df[feature].dtype =='object':
                    label_encoder = LabelEncoder()
                    df[feature] = label_encoder.fit_transform(df[feature])
                correlation = df[feature].corr(df['만족도'])
                correlations.append((feature, correlation))
            
            # 상관관계가 큰 특성 상위 3개 출력
            correlations.sort(key=lambda x: abs(x[1]), reverse=True)
            st.write("만족 여부와 가장 상관관계가 높은 특성:")
            for i in range(3):
                st.write(f"{correlations[i][0]}: {correlations[i][1]}")
             
        elif sati_pre == 0:
            st.write('### 불만족스러운 여행이셨군요...')
            img2 = Image.open('data/rage.jpg')
            st.image(img2)





if __name__ == '__main__':
    ml_st()