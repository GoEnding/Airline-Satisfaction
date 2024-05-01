import streamlit as st
from PIL import Image


# 데이터 불러오기
def home_st():
    
    st.write('<h1 style="text-align: center; color: skyblue; display: flex; align-items: center;"><img src="https://cdn.pixabay.com/photo/2014/08/27/14/33/aircraft-429200_1280.png" alt="plane" style="max-width: 1em; margin-right: 0.5em;"> 슬기로운 여행생활</h1>', unsafe_allow_html=True)
    st.write('<h2 style="text-align: center;">환영합니다!!',unsafe_allow_html=True)
    st.write('<h3 style="text-align: center;"> 여행의 만족도에 대한 데이터가 담겨있는 웹페이지입니다</p>', unsafe_allow_html=True)
    st.write('<h6 style="text-align: center;">데이터 분석 하기전에 데이터 소개를 먼저 봐주시고 둘러 보신다면 더욱 더 원할하게 볼 수 있습니다.',unsafe_allow_html=True)
    img = Image.open('./data/aircraft.jpg')

    st.image(img)


if __name__ == '__main__':
    home_st()