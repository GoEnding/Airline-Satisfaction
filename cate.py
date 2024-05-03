import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sb

def cate_st(selected_column):
    st.subheader('각 서비스에 대한 점수 데이터입니다.')
    st.info('승객점수 0:불만족 5:만족')
    df = pd.read_csv('data/Airline_sa.csv')
    font_path = 'c:\WINDOWS\Fonts\GULIM.TTC'  # 한글 폰트 파일의 경로를 지정합니다.
    font_prop = fm.FontProperties(fname=font_path)
    
    # 선택한 변수에 대한 바 차트를 그립니다.
    var_value = df[selected_column].value_counts()

    # 시각화
    fig, ax = plt.subplots(figsize=(9, 3))
    ax.bar(var_value.index, var_value.values)

    ax.set_xlabel("승객 점수", fontproperties=font_prop)
    ax.set_ylabel("빈도수", fontproperties=font_prop)
    ax.set_title(selected_column, fontproperties=font_prop)
    
    # 그림을 Streamlit 앱에서 표시합니다
    st.pyplot(fig)


    
    # 변수의 값 출력
    col1,col2 = st.columns([2,3])

    with col1 :
        st.write(f"{selected_column}:")
        st.write(var_value)
    with col2 :
        st.subheader('전체 만족도')
        fig, ax = plt.subplots()
        ax.pie(df['만족도'].value_counts(), labels=["Neutral or dissatisfied", "Satisfied"], colors=sb.color_palette("YlOrBr"), autopct='%1.1f%%')
        ax.axis('equal')  # 원형을 유지하기 위해 가로세로 비율을 동일하게 설정
        ax.legend()
        st.pyplot(fig)

# Streamlit 앱 실행
if __name__ == "__main__":
    # 데이터를 불러옵니다 (실제 데이터 파일 경로에 맞게 수정해야 합니다)
    df = pd.read_csv('data/Airline_sa.csv')
    
    # 사용자가 선택한 카테고리를 드롭다운 메뉴로 선택합니다
    selected_column = st.selectbox("카테고리를 선택하세요.", df.columns)
    
    # 선택한 카테고리에 대한 바 차트를 그립니다
    if selected_column:
        cate_st(selected_column)
    