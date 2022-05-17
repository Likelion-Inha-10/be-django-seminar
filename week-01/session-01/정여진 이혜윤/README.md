## 백엔드 장고 세션 첫번째 세미나 안내

### 📝 **학습목표**

장고의 기본적인 작동원리를 알 수 있다.

간단한 장고 웹서비스 개발 환경을 세팅할 수 있다.

### 📅 **일정 안내**

**5/18 (수) 오후 7시 오프라인** (5남 강의실)

### 📋 **과제 제출**

- 과제 제출은 **깃허브 레포지토리를 통하여 제출 예정**
- 레포지토리 내 **지정된 주차 및 페어별 폴더에 제출**
- **반드시 제출 폴더 및 주차를 지킬 것**
- 제출 형식 및 파일 개수 상관 없음
- **자신이 공부한 사항을 모두 제출**
- **다만, 가상환경 혹은 바이너리 파일 및 개인정보 위험이 있는 파일의 업로드 엄금**
- 각 세션 시작 **3시간 전 모든 과제 제출 마감**

### 🌲 **브랜치 관련 안내**

- **각 주차의 세션과 팀 페어 당 브랜치를 생성하여 관리**
- 만약 **`1주차 수요일(세션 1) 정승찬 김예은`** 페어라고 가정하였을 때 **브랜치명**은 `01-01-정승찬-김예은`으로 작성
- _**브랜치명을 반드시 준수할 것**_
- **_절대로, 어떠한 일이 있어도, 다른 페어의 파일을 수정하지 말 것. 자신의 페어 폴더만 수정하고 변경할 것._**
- **과제는 이미 생성되어 있는 1주차 수요일 (세션 1) 폴더에 있는 페어 폴더 안쪽**에 자유롭게 제출 후 PR 생성
- 브랜치 생성 방법과 PR 방법은 [이곳](https://github.com/Likelion-Inha-10/be-assignments-submit-practice/blob/main/README.md) 을 참조

### 🦁 페어 안내

- **정승찬 김예은**
- **정여진 이혜윤**
- **정민경 김홍진**
- **이민성 이한주**

### 🏆 학습 범위

- **페어 전원**
  - **코드라이언 | 일단 만드는 Django**
    - **Chapter1** | Intro
    - **Chapter2** | Django와 친해지기

## 아래에 내용을 작성하십시오.

> ## FRAMEWORK

- 웹 서비스 개발을 쉽게 만들어주는 기계. **틀**.

- 명확한 목적을 달성하기 위해 코드를 재사용 가능한 형태로 구조화

- 어떤 프로그램을 쉽게 만들기 위한 요소와 룰을 제공해 줌으로서 소프트웨어의 생산성과 품질을 높이는 역할
- ex. Spring, Django, Ruby on Rails

> ## LIBRARY

- 소프트웨어를 개발하기 쉽게 어떤 기능을 제공하는 **도구**들

- 프레임워크에서 제공하는 요소와 그것을 사용하기 위한 규약을 지키면 그 밖에 **어떤 라이브러리를 가져다가 써도, 어떤 패키지를 가져다가 써도 상관X** ( 프레임워크와의 차이점 )

> ## WEB

- **web service** : html과 url을 미리 준비해놓고 사용자 요청에 대한 응답을 보낼 수 있는 프로그램

- **web server** : html 문서를 구성하는 각종 웹페이지 리소스(CSS,Javascript,img)등의 공유 저장소 역할
- **HTTP** : HyperText Transfer Protocol. 하이퍼텍스트(HTML)를 빠르게 교환하기 위한 통신(프로토콜). 서버와 클라이언트(웹 브라우저를 사용하는 사람)의 사이에서 어떻게 메시지를 교환할 지를 정해 놓은 규칙.

  - ### GET : 데이터를 단순 조회 (DB에 추가적인 정보 처리 X)
  - ### POST : 데이터를 서버로 제출해서 생성 또는 수정

> ## 가상 환경

- 자신이 원하는 Python 환경을 구축하기 위해 필요한 버전, 모듈만 담아 놓는 바구니

▶ 생성

    python -m venv myvenv

▶ 실행

    source myvenv/Scripts/activate

▶ 종료

    deactivate

> ## 디자인 패턴
>
> ▶ MVC ( Model - View - Controller )

- Model 데이터베이스와 상호작용 담당
- View: 사용자 인터페이스 담당
- Controller: 웹서비스 내부의 논리 담당

▶ MTV (Model - Template - View)

- Model: 데이터베이스와 상호작용 담당
- Template: 사용자 인터페이스 담당
- View: 웹서비스 내부 동작의 논리를 담당

▶ MVVM (Model - View - ViewModel)

▶ MVP (Model - View - Presenter)

> ## DJANGO & MTV

- Model

  모델은 클래스로 정의되며 하나의 클래스가 하나의 DB Table

  원래 DB를 조작하기 위해선 SQL을 다룰 줄 알아야 하지만 장고는 ORM(Object Relational Mapping)기능을 지원하기 때문에 파이썬 코드로 DB를 조작 가능

- Template

  뷰에서 로직을 처리한 후 html 파일을 context와 함께 렌더링

  장고는 자체적인 Django Template 문법을 지원하며 이 문법 덕분에 html 파일 내에서 context로 받은 데이터를 활용 가능

- View

  MVC 패턴의 컨트롤러에 대응되며 요청에 따라 적절한 로직을 수행하여 결과를 템플릿으로 렌더링하며 응답

> ## DJANGO 구조

---

## settings.py

- INSTALLED_APPS

  프로젝트에서 사용할 앱들의 경로가 위치하는 영역
  user defined app의 경로도 이 항목에 포함된다

- TEMPLATES

  공통적으로 들어가는 html코드를 관리하기 위한 확장형 template들의 경로를 설정하는 영역

- DATABASES

  database를 사용하기 위한 설정이 위치하는 영역
  default로 sqllite를 사용한다

- TIME_ZONE

  django의 DateTime객체에서 사용할 기준시를 설정하는 영역

- STATIC_URL
  CSS, Image등 의 정적 파일 경로를 설정하는 영역

## urls.py

-     urlpatterns 리스트의 항목(엔드포인트, 대상)에 따라 request를 라우팅 한다
- http://127.0.0.1:8000/ 뒤에 어떤 경로 ?

         urlpatterns=[
           path('admin/',admin.site.urls),
           path('',include('users.urls'))
         ]

       ▶엔드포인트가 admin/인 request에 대해서는 장고 기본 admin urls을 라우팅,

  ▶엔드포인트가 없는 request에 대해서는 users라는 앱의 urls를 라우팅한다

## manage.py

1.  서버 켜기

        python manage.py runserver

2.  application 만들기

        python manage.py startapp

3.  Database 초기화 및 변경사항 반영

        python manage.py migrate

4.  관리자 계정 만들기

        python manage.py createsuperuser

> ## django 실습 [ 가상환경에서 django를 이용한 프로젝트]

1.  python -m venv myvenv (가상환경 생성)
2.  source myvenv/Scripts/activate (가상환경 실행)
3.  pip install django
4.  pip freeze (django 설치 여부 확인)
5.  django-admin startproject 프로젝트명
6.  cd 프로젝트명
7.  ls (선택사항)(manage.py 가 있는 것을 확인)
8.  clear (선택사항)
9.  python manage.py runserver (ctrl+C : 페이지 닫기)
10. python manage.py startapp 어플리케이션명
    (앱은 django의 작은 단위)
11. settings.py에 방금 새로만든 어플을 등록
    ( 클래스명자체를 등록시키는게 더 안전 : 어플리케이션명.apps.클래스명)
12. 어플리케이션 폴더 내에 templates 라는 새로운 폴더 생성 후 index.html 파일 생성
13. index.html 에 내용 작성
14. 어플리케이션 폴더 내에 view.py에 함수 작성

        def 함수명(request):

        return render(request,'index.html')

        # request 요청 시, 요청 사항과 함께 해당 파일 내용을 보여준다.

15. urls.py에 이 함수가 언제 실행될지를 명시

    ▶ urls.py: 어떤 url이 들어왔을 때 view.py의 어떤 함수를 실행시킨다는 것을 명시해놓는 파일

- path(’경로’,’어플리케이션명.views.함수명’,name=’url이름’), 작성

- import 어플리케이션명.views 작성
