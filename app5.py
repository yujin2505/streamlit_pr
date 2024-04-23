#이미지/동영상/음악파일을 화면에 보여주는 방법

import streamlit as st

#이미지 처리를 위한 라이브럴
from PIL import Image #파이썬 이미지 라이브러리 PIL

def main():
    # 1. 저장되어있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg') 
    
    st.image(img)
    st.image(img, width=500)
    st.image(img, width=True) #width=True해주면 자동으로 폭을 맞춰준다

    #2. 인터넷상에 있는 이미지를 화면에 표시하는 방법 인터넷상의 이미지:URL이 있다
    
    url = 'https://i.imgur.com/QgWbK9D.gif'
    st.image(url)
    
    video_file = open('./data/video1.mp4','rb')
    st.video(video_file)
    
if __name__ == '__main__':
    main()

