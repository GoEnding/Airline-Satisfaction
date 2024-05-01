import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

def corr_st():
    df = pd.read_csv('data/Airline_sa.csv')
    df = df.iloc[ : ,1:]
    choice_list = st.multiselect('원하는 컬럼을 선택하세요',df.columns)
    if len(choice_list) != 0 :
        st.dataframe(df[choice_list])
        st.dataframe(df[choice_list].corr(numeric_only=True))
    else :
        st.write()

if __name__ == '__main__':
    corr_st()