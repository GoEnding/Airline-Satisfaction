import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.font_manager as fm
def corr_st():
    # 데이터 불러오기
    df = pd.read_csv('data/Airline_sa.csv')
    df = df.iloc[ : , 1: ]
    font_path = 'c:/Windows/Fonts/gulim.ttc'  # 한글 폰트 파일의 경로를 지정합니다.
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

    # 선택한 컬럼들을 멀티셀렉트로 받기



    tab1,tab2 = st.tabs(['전체 상관관계','만족도 대비 상관관계'])
    

    # 컬럼이 선택되었을 경우에만 실행
    with tab1:
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

    with tab2:
        choice_column = st.selectbox('컬럼을 선택하세요', df.select_dtypes(include=['float64', 'int64']).columns)

        if len(choice_column) != 0:
            st.dataframe(df[['만족도', choice_column]].corr())

            # 산점도로 사용자에게 보여주자
            fig, ax = plt.subplots()
            sb.regplot(x=df['만족도'], y=df[choice_column], fit_reg=True, ax=ax)
            plt.title(f'만족도와 {choice_column}의 산점도', fontsize=20, fontproperties=font_prop)
            plt.xlabel('만족도', fontproperties=font_prop)
            plt.ylabel(choice_column, fontproperties=font_prop)
            st.pyplot(fig)

if __name__ == '__main__':
    corr_st()
