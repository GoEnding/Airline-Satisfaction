import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from matplotlib import font_manager, rc
import platform
from PIL import Image
def corr_st():
    plt.rcParams['axes.unicode_minus'] = False
    if platform.system() == 'Linux':
        rc('font', family='NanumGothic')
    elif platform.system() == 'Windows':
        # 윈도우 환경에서 한글 폰트 설정
        font_path = "c:\WINDOWS\Fonts\GULIM.TTC"  # 한글 폰트 파일 경로
        font_name = font_manager.FontProperties(fname=font_path).get_name()
        rc('font', family=font_name)
    # 데이터 불러오기
    df = pd.read_csv('data/Airline_sa.csv')
    df = df.iloc[ : , 1: ]


    tab1,tab2 = st.tabs(['만족도 대비 상관관계','일부 시각화 자료'])
    

    with tab1:
        st.info('비례,관계없음,반비례를 차례대로 나타낸 예시입니다.')
        img = Image.open('./data/비례반비례.png')
        st.image(img)
        choice_column = st.selectbox('컬럼을 선택하세요', df.iloc[ : ,  :-1 ].columns)


        df['만족도'] = df['만족도'].replace({'satisfied' : 1 , 'neutral or dissatisfied' : 0} )
        

        if df[choice_column].dtype == 'object':
            label_encoder = LabelEncoder()  
            df[choice_column] = label_encoder.fit_transform(df[choice_column])

        col3, col4 = st.columns([2, 3])    
        with col3:
            st.dataframe(df[['만족도', choice_column]].corr(numeric_only=True))
                    
        with col4:
            st.info('※0.3이상:비례※-0.3이하:반비례※나머지:상관없음')
            correlation = df[['만족도', choice_column]].corr().iloc[0, 1]
            # 상관관계에 따라 다른 메시지 표시
            if correlation >= 0.3:
                st.write("### 비례 관계입니다.")
            elif correlation <= -0.3:
                st.write("### 반비례 관계입니다.")
            else:
                st.write("### 상관이 크게 없습니다.")

            # 산점도로 사용자에게 보여주자  
        fig, ax = plt.subplots()
        sb.regplot(x=df['만족도'], y=df[choice_column], fit_reg=True, ax=ax)
        plt.title(f'만족도와 {choice_column}의 상관관계', fontsize=20)
        plt.xlabel('만족도')
        plt.ylabel(choice_column)
        st.pyplot(fig)


    with tab2:

        selected_column = st.selectbox("일부 서비스에 있어서 비행거리에 대한 만족도 차트입니다.", ['다리 공간 서비스', '좌석 편안함', '클래스'])

        if selected_column:
            fig, ax = plt.subplots(figsize=(10, 6))
            sb.barplot(data=df, x=selected_column, y='비행 거리', hue='만족도', ax=ax)
            ax.set_title(f"{selected_column} 에있어서 비행거리에 대한 만족도 차트")
            ax.set_xlabel(selected_column)
            ax.set_ylabel('비행 거리')
            ax.legend(title='만족도')
            plt.xticks(rotation=45)
            st.pyplot(fig)

        
if __name__ == '__main__':
    corr_st()
