# 차트 그리기 방법

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def main():
    st.title('차트 그리기 1')
    
    df = pd.read_csv('./data/iris.csv')
    
    st.dataframe(df)
    
    # sepal_length 와 sepal_width의 관계를 차트로 나타내시오
    
    fig1 = plt.figure()
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig1)
    
    fig2 = plt.figure()
    sb.scatterplot(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig2)
    
    fig3 = plt.figure()
    sb.regplot(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig3)
    
if __name__ == '__main__' :
    main()