import streamlit as st
from corr import corr_st
from eda import eda_st
from home import home_st
from ml import ml_st
from cate import cate_st



def main():

    menu = ['Home','각 만족도', '상관관계분석', 'EDA','만족도 예측']

    choice = st.sidebar.selectbox('메뉴',menu)

    if choice == menu[0]:
        home_st()
    elif choice == menu[1]:
        selected_column = st.selectbox("Select a category", ['Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking', 'Gate location', 
                 'Food and drink', 'Online boarding', 'Seat comfort', 'Inflight entertainment', 'On-board service', 
                 'Leg room service', 'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness'])
        # 사용자가 컬럼을 선택한 후에 cate_st() 함수를 호출합니다
        if selected_column:
            cate_st(selected_column)

    elif choice == menu[2]:
        corr_st()
    elif choice == menu[3]:
        eda_st()
    elif choice == menu[4]:
        ml_st()
if __name__ == '__main__':
    main()