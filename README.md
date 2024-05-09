# Airline-Satisfaction

출처

항공사 승객 만족도 데이터
https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction/data

크롬에서 해야하며 아나콘다 다운,파이썬 다운로드 등 여러 환경 셋팅을 했습니다.
데이터 가공을 위해 쥬피터 노트북을 다운받습니다(데이터 가공 및 인공지능 개발 환경 할 수 있는 툴)
그 후 깃 허브에서 레파지토리를 하나 생성해줍니다.
그러면서 깃허브 데스크탑도 안깔려있으면 다운 받아줍니다.
이제 깃 허브에서 open with Desktop을 눌러 클론을 해주거나
깃 허브 데스크탑을 직접 눌러 File 누른 후 경로를 복사해 클론을 해줍니다.
그 다음 그 파일 경로로 가서 data 폴더라는 새폴더를 만들어 줍니다.(이곳에 가공할 데이터를 넣어 줄 것입니다.)
아나콘다 프롬프트를 키고 "cd 경로명"을 해주면 그 경로로 갑니다.
그 후 "jupyter notebook ." 을 그대로 쳐주면 쥬피터 노트북이 실행이 됩니다.
거기서 가져온 데이터를 가공해줍니다.가공이 완료 되면 
다시 Git hub Desktop으로 가서 open in visual studio code를 열어줍니다.
그 다음 가상환경을 설정해 줄 것입니다.
먼저 
conda create -n 가상환경이름 python=3.10 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn
을 함으로써 가상환경 생성 및 여러 라이브러리를 설치해줍니다.
그 다음
conda activate 가상환경이름 을 해주면 가상환경으로 들어가집니다.
그 다음 VSC 다시 켜고 가상환경으로 진입해줍니다.
가상환경에서 pip install streamlit 해서 streamlit 을 다운 받아주고
파일은 하나 만들어 streamlit run 을 해서 잘 켜지는지 확인 후 streamlit 라이브러리를 통해 웹 브라우저 프론트 백엔드 부분을 개발했습니다.


