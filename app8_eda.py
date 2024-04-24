import streamlit as st
import pandas as pd

def run_eda():
    st.subheader('EDA 화면')
    
    # iris.csv 파일을 읽어와서 여러 컬럼들 선택 가능토록 하여 선택한 컬럼들만 화면에 보여주고 상관계수도 보여주도록 개발
    df = pd.read_csv('./data/iris.csv')
    st.dataframe(df)
    
    # 모든 수치형 변수에 대한 상관 계수 계산
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    selected_cols = st.multiselect('원하는 컬럼을 선택하세요', numerical_cols)
    
    if selected_cols:
        corr_df = df[selected_cols].corr()
        st.write("선택한 컬럼들 간의 상관 관계:")
        st.write(corr_df)
    else:
        st.write("컬럼을 선택하세요.")
    