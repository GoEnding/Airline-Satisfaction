import streamlit as st
import joblib
import numpy as np
import pandas as pd

def ml_st():
    st.title('만족도 예측하기')
    # 1. 예측하기 위해서 유저한테 입력받는다.
    st.text('성별을 선택하세요.')
    gender = st.radio('성별 선택', ['남자','여자'])
    if gender =='남자' :
        gender = 1
    elif gender == '여자' :
        gender = 0

    st.text('고객 유형은 무엇인가요?')
    Customer_type = st.radio('고객 유형',['Loyal Customer','disLoyal Customer'])
    if Customer_type == 'Loyal Customer':
        Customer_type = 1
    elif Customer_type == 'disLoyal Customer':
        Customer_type = 0
    
    st.text('나이를 입력해주세요')
    age = st.number_input('나이 입력', min_value=0, max_value=100, value= 24)

    st.text('비행목적은 무엇인가요?')
    travel_type = st.radio('목적 선택',['Business travel','Personal Travel'])
    if travel_type == 'Business travel':
        travel_type = 0
    elif travel_type == 'Personal Travel':
        travel_type = 1

    st.text('비행 클래스는 무엇인가요?')
    Class = st.radio('클래스 선택',['Business','Eco','Eco Plus'])
    if Class == 'Business':
        Class = 0
    elif Class == 'Eco':
        Class = 1
    elif Class == 'Eco Plus':
        Class = 2   

    

    # 2. 입력 받은 것을 리스트로 정렬 한다.
    # 3. 그 값을 머신러닝에 넣어서 예측 할 수 있도록 한다.

if __name__ == '__main__':
    ml_st()