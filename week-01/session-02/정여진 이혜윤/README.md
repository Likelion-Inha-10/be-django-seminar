# 피드백
# [1] url.py에서 include의 역할은?
### [1-1] 라우팅

- 라우팅(Rouing)이란 네트워크 상에서 데이터를 전달할 때, 목적지까지의 경로를 체계적으로 결정하는 경로 선택 과정

### [1-2] 언제까지 무한 import ??? url 효율적으로 관리하기

- 만약, 장고 프로젝트가 매우 커진다면 하나의 urls.py에서 관리 불가 ㅠㅠ

- 그러므로 애플리케이션마다 urls.py를 생성해 프로젝트 urls.py에 연결해 관리

- 프로젝트 urls.py와의 차이점은 경로(Path)에 users가 존재X

- users 경로를 접근했을 때, include('first_app.urls') 경로의 first_app/urls.py로 이동해 접근합니다. 즉, users로 이동했을 때 URL 경로를 재 탐색하므로, first_app/urls.py에는 users를 작성하지 않습니다.

### [1-3] user App내의 url.py에서 view 함수 호출하기

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

### [1-4] 메인 프로젝트 urls에서 include 하여 넘겨주기

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

### [1-5] 요약: path 함수의 2가지 사용

        path(route, view, kwargs=None, name=None)

        #1 path('user',include('users.urls'))
        django urls의 include를 사용해, 다른 app의 url로 넘겨주어 사용

        #2 path('/sign-in',view.SignInView.as_view(),name='login')

        특정 값을 직접 지정.
        특정 패턴을 찾으면 해당 패턴에 대해 view 함수를 호출,

        지정한 Template이 있으면 name=''으로 rendering이 가능
        (앱마다 동일한 이름의 index.html 사용할 경우에는
        별도의 template 파일 생성 필요)

# [2] view.py에서 render의 역할은?

        def 함수명(request):

        return render(request,'index.html')

        # request 요청 시, 요청 사항과 함께 해당 파일 내용을 보여준다

- view는 특정 기능을 제공하고 특정한 템플릿을 가진, Django 어플리케이션에 있는 웹 페이지의 type이다. 예를 들어, 블로그 어플리케이션에서는\
    - Blog 홈페이지: 가장 최근의 항목들을 보여줌\
    - 어떤 항목의 세부 페이지\
    - 년도 별 페이지: 주어진 연도의 모든 항목을 표시\
와 같은 view를 가질 수 있다

- Django에서는 웹페이지와 기타 콘텐츠가 view로 전달된다. 각 view는 파이썬 함수나 클래스로 표현된다

- view는 요청된 페이지의 내용이 담긴 HttpResponse 객체를 반환해야 한다
(HttpResponse는 HTML 문자열 및 이미지 등 다양한 응답을 wrapping함)
이 때 HttpResponse 객체를 반환하는 방식으로 render() 함수가 자주 쓰인다

        render(request, template_name)

- request 객체를 첫번째 인수로 받고, 템플릿 이름을 두번째 인수로 받으면 해당 템플릿의 HttpResponse 객체가 반환된다.
(request는 Http 요청이 보내졌을 때에 Django가 만든 객체)

- [참고]( https://docs.djangoproject.com/ko/4.0/intro/tutorial03/)

# [3] settings.py에서 클래스명을 명시하여 등록하는 이유는?

### [3-1] AppConfig
어플리케이션의 한 클래스인데 해당 어플리케이션의 meta-data를 담고 있다. (app의 이름, 경로 등)

### [3-2] INSTALLED_APPS에 앱의 클래스를 명시하는 방식의 좋은 점
 - 클래스에서 app의 이름이나 경로를 변경함으로써 앱을 더 쉽게 구성할 수 있음
 - 클래스를 하위 분류하는 AppConfig를 여러 개 만들 수 있도록 함
 이 밖에도 여러 이점이 있어서 권장됨

### [3-3] 이전 버전과의 호환성 문제
- Django 1.7버전부터 앱들이 INSTALLED_APPS로 관리됨\
그리고 이전 버전과의 호환을 위해 default_app_config 변수가 추가됨
- INSTALLED_APP에서 AppConfig를 명시하지 않는다면 Django는 해당 app의 __init__.py 파일에서 default_app_config 변수를 확인해서 실행함\
 이 변수가 없다면 1.6버전의 방식으로 App이 수행됨
 이 때 프로그램의 수행이 default_app_config를 찾는 데 의존한다는 문제가 있음
- Django 3.2부터 자동 AppConfig 검색 기능이 추가됨에 따라 default_app_config의 사용이 중단됨\
하지만 이전 버전과 비호환성 문제와 다른 목적을 위해 설계된 클래스를 가져올 수 있다는 문제가 있을 수 있음

- [참고1](https://docs.djangoproject.com/en/4.0/releases/3.2/) / [참고2](https://code.djangoproject.com/ticket/31180)