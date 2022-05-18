
## 📌 가상 환경에서 Django 프로젝트 생성하기

- 독립적인 가상 환경에서 프로젝트를 만들어 봅시다.

### 📌 가상 환경을 만들고, 그 안에 django 프로젝트를 생성하기

> python -m venv 가상환경이름
   
   - 가상 환경 만들기

> source 가상환경이름/Scripts/activate
  
  - 생성한 가상 환경 실행하기
  
  - 가상환경 안의 Scripts 폴더 안의 activate 파일을 실행시키겠다는 것
  - ![image](https://user-images.githubusercontent.com/103047410/168937361-3634e12f-4d04-47ec-a3da-aeef3f8490f7.png)


> pip install django
   
   - django 패키지를 설치 

![image](https://user-images.githubusercontent.com/88240193/168769283-dad33fcc-1853-4586-8fac-187e3d32a24e.png)

> pip freeze
   
   - 어떤 패키지가 설치되어 있는지를 출력

> django-admin startproject 프로젝트이름
   
   - 장고 프로젝트를 생성

![image](https://user-images.githubusercontent.com/88240193/168725087-f4d64a42-c6e6-487f-964a-4faadc8e2fc9.png)


---



## 📌 파이썬 파일 분석


### 1. __init__.py

- 해당 파일을 담고있는 폴더 project1 이 패키지임을 알려주는 기능

---

### 2. urls.py

- 각종 url 들을 등록 및 관리해주는 파일

- 우리가 설계한 URL에 대해서 요청이 들어왔을 때 어떤 동작을 수행할지와, 어떤 URL 들을 관리할 것인지를 써주는 파일입니다.

- 기본 URL 뒤에다 슬래쉬 '/' 로 다른 URL 들을 설계 가능
    
EX) 기본 URL : "www.codelion.net" 일때
=> www.codelion.net/login , www.codelion.net/classroom/, www.codelion.net/classroom/10 과 같은 URL 을 설계 가능

![image](https://user-images.githubusercontent.com/103047410/168953804-59d90839-21cf-4fe3-b275-7319a2b2076b.png)

![image](https://user-images.githubusercontent.com/103047410/168955118-8f51878b-c142-4c84-bdd6-e1763b91a84b.png)

![image](https://user-images.githubusercontent.com/103047410/168955384-9118587f-0a6f-4d09-a024-b4b0a8bfca4e.png)

---

## 3. manage.py

### 기능 요약
      1) 서버 켜기
      2) 어플리케이션 만들기 => 프로젝트를 구성하는 요소들이 어플리케이션, 즉 앱이라 할 수 있는데 그 앱들을 만들 수 있습니다.
      3) DB 초기화 및 변경사항 반영
      4) 관리자 계정 만들기



### 상세

#### 1. 서버 켜기

> $ python manage.py runserver 
>> 서버를 실행시키는 명령어

ex) Starting development server at http://127.0.0.1:8000/ 
=> 웹 사이트 주소. 해당 주소에 장고 서버가 실행됩니다.

---

#### 2. 어플리케이션 만들기

> $ manange.py startapp 앱이름

- 어플리케이션 : 장고 프로젝트를 이루는 단위.
- 즉, 장고로 만들어진 웹 서비스는 어플리케이션 여럿이 모여서 만들어진 결과물

- ex) 쇼핑물 웹서비스 : 게시판 기능 + 결재 기능 + 장바구니 기능
각각에 대해 앱을 만들어서 쇼핑몰 프로젝트 안에 담는것이 효율적!

- 앱을 생성후 장고 프로젝트가 인식할 수 있도록 INSTALLED_APPS 에다 등록해줘야 합니다.
- (myapp 이라는 어플 예시)
![image](https://user-images.githubusercontent.com/103047410/168935619-1262a0c3-5882-49a1-96de-5ec874b7d61a.png)
![image](https://user-images.githubusercontent.com/103047410/168935924-570d0519-0745-4ced-a522-4f8e74ca5be7.png)


---

#### 3. DB 초기화 및 변경사항 반영

> $ python manage.py migrate 
>> DB를 초기화 해주거나, 해당 프로젝트에서 DB를 변경할 일이 생기면 변경된 사항을 알려주는 기능입니다. 

-db.sqlite3 라는 DB를 초기화 해주거나, 해당 프로젝트에서 db.sqlite3 데이터베이스를 변경할 일이 생기면 변경해줍니다.
(dq.sqlite3 : 장고에서 기본적으로 제공하는 DB)

---

#### 4. 관리자 계정 만들기

> $ python manage.py createsuperuser
>> 관리자 계정을 만들 수 있게 해줍니다.

- 웹서비스에 대한 관리자 계정을 생성하고 로그인후, 해당 웹서비스의 관리자로서 관리할 수 있게 됩니다.
![image](https://user-images.githubusercontent.com/103047410/168936393-6d2fb651-7b2c-485f-bd06-c56fe97232b5.png)

