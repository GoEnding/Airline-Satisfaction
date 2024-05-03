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

    # 데이터 불러오기
    df = pd.read_csv('data/Airline_sa.csv')
    df = df.iloc[ : , 1: ]


    # 선택한 컬럼들을 멀티셀렉트로 받기



    tab1,tab2 = st.tabs(['만족도 대비 상관관계','전체 상관관계'])
    

    # 컬럼이 선택되었을 경우에만 실행


    with tab1:
        st.info('비례,관계없음,반비례를 차례대로 나타낸 예시입니다.')
        img = Image.open('./data/비례반비례.png')
        st.image(img)
        choice_column = st.selectbox('컬럼을 선택하세요', df.columns)
        df['만족도'] = df['만족도'].replace({'satisfied' : 1 , 'neutral or dissatisfied' : 0} )
        

        if len(choice_column) != 0:
            if df[choice_column].dtype == 'object':

                label_encoder = LabelEncoder()  
                df[choice_column] = label_encoder.fit_transform(df[choice_column])


            st.dataframe(df[['만족도', choice_column]].corr(numeric_only=True))

            # 산점도로 사용자에게 보여주자  
            fig, ax = plt.subplots()
            sb.regplot(x=df['만족도'], y=df[choice_column], fit_reg=True, ax=ax)
            plt.title(f'만족도와 {choice_column}의 상관관계', fontsize=20)
            plt.xlabel('만족도')
            plt.ylabel(choice_column)
            st.pyplot(fig)


    with tab2:
        choice_list = st.multiselect('원하는 컬럼을 선택하세요', df.columns)
        if len(choice_list) != 0:
            st.dataframe(df[choice_list])
            # 선택한 컬럼들만 포함하는 데이터프레임 생성
            df_selected = df[choice_list].copy()

            # 범주형 변수를 레이블 인코딩으로 변환
            label_encoder = LabelEncoder()
            for col in df_selected.select_dtypes(include=['object']).columns:
                df_selected[col] = label_encoder.fit_transform(df_selected[col])

            # 범주형 변수에 대해 원핫 인코딩 적용
            ct = ColumnTransformer([('encoder', OneHotEncoder(), df_selected.select_dtypes(include=['object']).columns)], remainder='passthrough')
            df_encoded = pd.DataFrame(ct.fit_transform(df_selected), columns=ct.get_feature_names_out())

            # 상관관계 계산
            corr_matrix = df_encoded.corr()

            # 상관관계 행렬 출력
            st.write(corr_matrix)

            if len(choice_list) >= 2 :
                # 1. 페어플롯을 그린다.

                fig1 =sb.pairplot(data = df, vars = choice_list)
                st.pyplot(fig1)
            else :
                st.text('컬럼은 2개 이상 선택해야 합니다.')


if __name__ == '__main__':
    corr_st()
