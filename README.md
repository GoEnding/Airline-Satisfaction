# 항공사 승객 만족도 EDA 및 분석

## 환경 설정

- 크롬에서 아나콘다 및 파이썬을 다운로드하여 설치합니다.
- 데이터 가공 및 인공지능 개발을 위해 쥬피터 노트북을 설치합니다.

## 깃허브 레포지토리 생성

- 깃허브 레포지토리를 생성합니다.
- 깃허브 데스크탑을 설치하지 않은 경우 설치합니다.

## 로컬에서 클론

- 깃허브에서 Desktop을 통해 클론하거나 직접 깃허브 데스크탑에서 파일 경로를 복사하여 클론합니다.
- 클론한 경로로 이동한 후 데이터를 저장할 새 폴더(data)를 생성합니다.

## 데이터 가공

- 아나콘다 프롬프트를 열고 해당 경로로 이동합니다.
- 쥬피터 노트북을 실행합니다.
- 데이터를 가공합니다.

## 가상환경 설정

- 새로운 가상환경을 생성하고 필요한 라이브러리를 설치합니다.
  ```bash
  conda create -n 가상환경이름 python=3.10 openssl numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn

 - 가상환경을 활성화합니다.
 - conda activate 가상환경이름
- Visual Studio Code(VSC)를 열고 해당 가상환경으로 전환합니다.

## Streamlit 설치
- 가상환경에서 Streamlit을 설치합니다. (예: pip install streamlit)
- 파일을 생성하고 Streamlit을 실행하여 정상 작동을 확인합니다. (예: streamlit run 파일이름)
