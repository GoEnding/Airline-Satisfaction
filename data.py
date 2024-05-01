import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def data_st():
    
    df = pd.read_csv('./data/Airline_sa.csv')
    df = df.iloc[ : , 1 : ]
    tab1, tab2= st.tabs(['Tab A' , 'Tab B']) 
        # 데이터 출력을 위한 토글 버튼
    with tab1:    
        if 'show_data' not in st.session_state:
            st.session_state.show_data = False  # 세션 상태에 show_data 변수가 없으면 False로 초기화

        show_data = st.button('## 데이터 미리보기')

    # 버튼이 눌린 경우에만 데이터를 출력하도록 설정
        if show_data:
            st.session_state.show_data = not st.session_state.show_data  # 버튼을 토글하여 상태 변경

    # show_data가 True인 경우에만 데이터 출력
        if st.session_state.show_data:
            st.write(df)


if __name__ == '__main__':
    data_st()