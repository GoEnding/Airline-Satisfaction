import streamlit as st
from corr import corr_st
from eda import eda_st
from home import home_st
from ml import ml_st
from cate import cate_st



def main():

    menu = ['Home','EDA 및 데이터분포','각 만족도', '상관관계분석','만족도 예측']

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        home_st()
    elif choice == menu[1]:
        eda_st()     

    elif choice == menu[2]:
        selected_column = st.selectbox("카테고리를 선택하세요.", ['기내 와이파이 서비스', '출발/도착 시간 편의성', '온라인 예약 편의성', '탑승구 위치', 
                 '음식과 음료', '온라인 탑승', '좌석 편안함', '기내 엔터테인먼트', '탑승 서비스', 
                 '다리 공간 서비스','수하물 처리', '체크인 서비스', '기내 서비스', '청결도'])
        # 사용자가 컬럼을 선택한 후에 cate_st() 함수를 호출합니다
        if selected_column:
            cate_st(selected_column)
     
    elif choice == menu[3]:
        corr_st()
    elif choice == menu[4]:
        ml_st()
if __name__ == '__main__':
    main()