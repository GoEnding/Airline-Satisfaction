import streamlit as st
from PIL import Image


# 데이터 불러오기
def home_st():
    
    st.write('<h1 style="text-align: center; color: skyblue; display: flex; align-items: center;"><img src="https://cdn.pixabay.com/photo/2014/08/27/14/33/aircraft-429200_1280.png" alt="plane" style="max-width: 1em; margin-right: 0.5em;"> 슬기로운 여행생활</h1>', unsafe_allow_html=True)
    st.write('<h2 style="text-align: center;">환영합니다!!',unsafe_allow_html=True)
    st.write('<h3 style="text-align: center;"> 한 항공사의 만족도 데이터가 담겨있는 웹페이지입니다</p>', unsafe_allow_html=True)
    st.write('<h6 style="text-align: center;"> 항공사가 만족하기 위해 필요한 데이터가 무엇인지 알아 볼 수 있는 웹페이지입니다.',unsafe_allow_html=True)
    img = Image.open('data/plane_travel.png')
    st.link_button('출처:https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data',url='https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data',use_container_width=True)

    st.image(img)


if __name__ == '__main__':
    home_st()