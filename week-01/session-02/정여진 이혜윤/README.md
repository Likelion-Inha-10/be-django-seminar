## 백엔드 장고 세션 두번째 세미나 안내

### 📝 **학습목표**

지난 세션에서의 질문에 답변을 할 수 있다.

운영진과 동료들과 토론을 통하여 다음 세션의 준비를 할 수 있다.

### 📅 **일정 안내**

**5/20 (금) 오후 7시 오프라인** **(5남 332)**

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
- 만약 **`1주차 금요일(세션 2) 정승찬 김예은`** 페어라고 가정하였을 때 **브랜치명**은 `01-02-정승찬-김예은`으로 작성
- _**브랜치명을 반드시 준수할 것**_
- **_절대로, 어떠한 일이 있어도, 다른 페어의 파일을 수정하지 말 것. 자신의 페어 폴더만 수정하고 변경할 것._**
- **과제는 이미 생성되어 있는 1주차 금요일 (세션 2) 폴더에 있는 페어 폴더 안쪽**에 자유롭게 제출 후 PR 생성
- 브랜치 생성 방법과 PR 방법은 [이곳](https://github.com/Likelion-Inha-10/be-assignments-submit-practice/blob/main/README.md) 을 참조

### 🦁 페어 안내

- **정승찬 김예은**
- **정여진 이혜윤**
- **정민경 김홍진**
- **이민성 이한주**

### 🏆 학습 범위

**페어 전원**

- 첫번째 세션에서의 질문에 대한 답변 준비하기 (**1주 2차시 폴더에는 답변을 위한 파일만** 준비하여 제출하기)
- **다음주 수요일 세미나 단단히 각오**하고 준비하기 (**다음주 수요일 세미나 자료는 week-02 session-01 폴더에 위치**)

## 피드백

## [1-1] 라우팅

- 라우팅(Rouing)이란 네트워크 상에서 데이터를 전달할 때, 목적지까지의 경로를 체계적으로 결정하는 경로 선택 과정

## [1-2] 언제까지 무한 import ??? url 효율적으로 관리하기

- 만약, 장고 프로젝트가 매우 커진다면 하나의 urls.py에서 관리 불가 ㅠㅠ

- 그러므로 애플리케이션마다 urls.py를 생성해 프로젝트 urls.py에 연결해 관리

- 프로젝트 urls.py와의 차이점은 경로(Path)에 users가 존재X

- users 경로를 접근했을 때, include('first_app.urls') 경로의 first_app/urls.py로 이동해 접근합니다. 즉, users로 이동했을 때 URL 경로를 재 탐색하므로, first_app/urls.py에는 users를 작성하지 않습니다.

## [1-3] user App내의 url.py에서 view 함수 호출하기

- Project의 urls.py 파일이 처음 들어오는 url을 구분하고 해당하는 App urls.py에 넘겨준 상태. 이제 다른 url을 가지고 목적에 맞게 함수를 불러올 차례 !

- http://127.0.0.1:8000/user/sign-in 이라는 url이 들어왔다고 가정 -> user App에서의 urls.py는 sign-in만을 바라보고 처리

       #users/urls.py

       from django.urls    import path
       from .              import views

       urlpatterns = [
           path('/sign-up',views.SignUpView.as_view()),
           path('/sign-in',views.SignInView.as_view()),
           path('/follow-user',views.FollowUserView.as_view()),
       ]

- user라는 url 계층은 전혀 보이지X. ->
- urlpatterns라는 list는 sign-in이라는 패턴을 순차적으로 탐색-> 그 결과로 두 번째에 있는 패턴이 실행 -> path 함수에서 import된 같은 디렉토리의 views.py 파일의 SignInView 클래스의 as_view 함수가 실행

## [1-4] 메인 프로젝트 urls에서 include 하여 넘겨주기

- **include** : 찾은 url 패턴에 대해 해당 어플리케이션 다른 urls 파일로 넘겨주는 역할
- **import path** : 라우팅할 경로를 설정할 수 있는 기능 가져오기

       #westagram/urls.py
       from django.contrib import admin
       from django.urls    import path,include

       urlpatterns = [
           path('user',include('users.urls')),
           path('post',include('posts.urls')),
       ]

- 직접 url pattern을 가지고 함수를 호출X
- user라는 단어가 있는 url을 만나면 include를 통해 user이라는 어플리케이션의 urls 파일로 넘겨줍니다.
- ex. url이 'user/sign-in'의 형태로 들어온다면 urlpatterns라는 list에서 넘겨받은 url의 첫 계층인 user가 보일 때 까지 하나씩 탐색
  user 다음에 오는 / <- 이 부분부터는 'users.urls' 파일에서 처리
  (user와 user/는 전혀 다른 엔드포인트)
- 만약 HTTP Request에 해당하는 url 패턴이 오지 않는다면 page not Found 에러로 처리

## [1-5] 요약: path 함수의 2가지 사용

        path(route, view, kwargs=None, name=None)

        #1 path('user',include('users.urls'))
        django urls의 include를 사용해, 다른 app의 url로 넘겨주어 사용

        #2 path('/sign-in',view.SignInView.as_view(),name='login')

        특정 값을 직접 지정.
        특정 패턴을 찾으면 해당 패턴에 대해 view 함수를 호출,

        지정한 Template이 있으면 name=''으로 rendering이 가능
        (앱마다 동일한 이름의 index.html 사용할 경우에는
        별도의 template 파일 생성 필요)
