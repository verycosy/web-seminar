# web-seminar
웹 세미나용 저장소입니다 !

### 갱신 이력
* **2020.07.20**    
    DOM 조작 기초
* **2020.07.28**    
  Python Flask 웹서버   

  1. 파이썬 가상환경 생성
        > python3 -m venv '가상환경이름'

  2. 파이썬 가상환경 활성화    
        > Windows: 가상환경이름\Scripts\activate.bat  
        Linux/MacOS : source 가상환경이름/bin/activate
  
  3. pip 업데이트 및 플라스크 설치
        > pip install --upgrade pip     
        pip install flask

  4. 패키지 관리
        > pip freeze > requirements.txt     
        pip install -r requirements.txt

  5. 플라스크 웹서버 실행     
        > Windows: set FLASK_ENV=development    
        Linux/MacOS : export FLASK_ENV=development    
        $ flask run