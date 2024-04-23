# 판다스 데이터 프레임을 웹 화면에 보여주는 방법

import streamlit as st
import pandas as pd

def main():
    df = pd.read_csv('data/iris.csv')
    
    #프린트 함수는 디버깅용
    print(df)
    
    st.dataframe()

if __name__ == '__main__' :
    main()