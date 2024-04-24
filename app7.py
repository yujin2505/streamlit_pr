# 파일을 업로드 하는 방법
# 이미지 파일 업로드, csv 파일 업로드

import streamlit as st
from datetime import datetime       # 현재시간을 가져와서 유니크한 파일명을 만드는데 사용할 목적으로 임포트
import pandas as pd
from PIL import Image


# 디렉토리 정보와 파일을 알려주면
# 해당 디렉토리에 파일을 저장하는 함수
def save_uploaded_file(directory, file):
    # 1. 디렉토리가 있는지 확인하여 없으면 디렉토리부터 만든다.
    import os
    if not os.path.exists(directory):
        os.makedirs(directory)
    # 2. 디렉토리가 존재하면, 파일을 저장한다.
    with open(os.path.join(directory, file.name), 'wb') as f: # with expression as 변수명 => 사용자가 close()를 하지 않아도 자동으로 파일을 닫아줌
        f.write(file.getbuffer())
    # 3. 저장이 완료되면 유저한테 알린다.
    return st.success(f"{file.name} 이 {directory} 에 저장되었습니다.")

def main():
    # 사이드바 만들기
    st.title('파일 업로드 프로젝트')

    sidebar_menu = ['이미지파일 업로드', 'csv 업로드', 'About']
    choice = st.sidebar.selectbox('메뉴', sidebar_menu) 

    if choice == sidebar_menu[0]: # 이미지파일 업로드 메뉴를 선택했을시
        st.subheader('이미지 파일 업로드!')
        file = st.file_uploader('이미지 파일을 선택하세요.', type=['jpg', 'png', 'jpeg']) # 이미지파일 형식을 하나만 허용할거면 그냥 쓰면 되고 여러개를 허용할시에는 [] 리스트로 작성
        
        if file is not None: # 유저가 올린 파일이 존재할때만 서버에 저장한다.
            print(file.name) # 파일 이름
            print(file.size) # 파일 크기
            print(file.type) # 파일 형식
            
            # 파일을 서버에 저장하기 위해서는 먼저!
            # 파일 이름을 유니크하게 만들어서 바꿔줘야 한다.
            # "현재시간 + 유저 아이디" 를 조합해서 만드는게 실무에서 가장 많이 사용
            current_time = datetime.now()
            new_filename = current_time.isoformat().replace(':', '_') + '.jpg'
            # .isoformat() 을 해주면 datetime형식을 문자열로 변환해줌
            # 파일명에는 :(콜론) 이 포함될 수 없음. => replace()를 이용하여 : 을 _ 로 바꿔줌
            # .jpg를 붙여서 jpg형식으로 통일해서 저장

            file.name = new_filename
            save_uploaded_file('image', file) # 파일을 image디렉토리에 저장

            # 이미지 업로드
            # 1. 첫번째 방법
            st.image(file, use_column_width=True) # use_column_width=True를 해주면 자동으로 폭을 맞춰줌
    
            # 2. 두번째 방법
            img = Image.open(file)
            st.image(img)


    elif choice == sidebar_menu[1]: # csv 업로드 메뉴를 선택했을시
        st.subheader('CSV파일 업로드!')
        csv_file = st.file_uploader('CSV 파일을 선택하세요', type='csv') # 이미지 업로드할때와 동일한 방식

        if csv_file is not None :

            # 파일명을 유니크 하게 만들어서 저장한다
            current_time = datetime.now()
            new_filename = current_time.isoformat().replace(':', '_') + '.csv' # 유니크한 파일명(현재시간)으로 저장
            csv_file.name = new_filename  # csv_file 이름을 new_filename으로 변경

            save_uploaded_file('data', csv_file)  # data디렉토리로 csv_file 저장

            st.dataframe(pd.read_csv(csv_file))


    elif choice == sidebar_menu[2]: # About 메뉴 선택시
        st.subheader('파일 업로드 프로젝트입니다.')

    else:
        pass

if __name__ == '__main__':
    main()