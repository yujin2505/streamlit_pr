#이미지/동영상/음악파일을 화면에 보여주는 방법

import streamlit as st

#이미지 처리를 위한 라이브럴
from PIL import Image #파이썬 이미지 라이브러리 PIL

def main():
    # 1. 저장되어있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg') 
    
    st.image(img)
    st.image(img, width=500)
    st.image(img, use_column_width=True) #width=True해주면 자동으로 폭을 맞춰준다

    #2. 인터넷상에 있는 이미지를 화면에 표시하는 방법 인터넷상의 이미지:URL이 있다
    
    #사진 파일
    url = 'https://miro.medium.com/v2/resize:fit:1000/format:webp/1*_ruPoPC4tiUP9Ojtiec4nw.gif'
    st.image(url)
    
    #동영상 파일
    video_file = open('./data/video1.mp4','rb')
    st.video(video_file)
    
    #오디오 파일
    audio_file = open('./data/song.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')
    
if __name__ == '__main__':
    main()


