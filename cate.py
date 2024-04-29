import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def cate_st(selected_column):
    df = pd.read_csv('data/Airline_sa.csv')
    
    # 선택한 변수에 대한 바 차트를 그립니다.
    var_value = df[selected_column].value_counts()

    # 시각화
    fig, ax = plt.subplots(figsize=(9, 3))
    ax.bar(var_value.index, var_value.values)

    ax.set_xlabel("Passengers Score")
    ax.set_ylabel("Frequency")
    ax.set_title(selected_column)
    
    # 그림을 Streamlit 앱에서 표시합니다
    st.pyplot(fig)
    
    # 변수의 값 출력
    st.write(f"{selected_column}:")
    st.write(var_value)

# Streamlit 앱 실행
if __name__ == "__main__":
    # 데이터를 불러옵니다 (실제 데이터 파일 경로에 맞게 수정해야 합니다)
    df = pd.read_csv('data/Airline_sa.csv')
    
    # 사용자가 선택한 카테고리를 드롭다운 메뉴로 선택합니다
    selected_column = st.selectbox("Select a category", df.columns)
    
    # 선택한 카테고리에 대한 바 차트를 그립니다
    if selected_column:
        cate_st(selected_column)