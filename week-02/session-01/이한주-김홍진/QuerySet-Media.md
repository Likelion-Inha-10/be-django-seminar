# DB에 있는 Blog객체들 html에 나타내기
- 썼던 글들을 admin페이지 말고 home(기본 url) 에 나타나게 하고싶다.
- (1) views.py 수정
- (2) index.html 수정

>![](https://velog.velcdn.com/images/97gkswn/post/9569eb75-0ced-4e7a-bbf0-79461c2a8c7d/image.png)

<br/>
<br/>

(1) views.py
>![](https://velog.velcdn.com/images/97gkswn/post/16d525aa-f135-461a-a410-4e3c7e39a043/image.png)<br/> 
>- views.py에 가서 home 메소드를 수정
>- 블로그라는 객체를 모두 가져와 posts변수에 저장
>- render의 세 번째 인자에 딕셔너리형태로 넘겨줌

(2) index.html
>![](https://velog.velcdn.com/images/97gkswn/post/82059032-7bfe-4e02-9eb4-e3ba5f52cbd3/image.png)

<br/>
<br/>

>-실제 웹페이지 화면
>![](https://velog.velcdn.com/images/97gkswn/post/35607e63-d114-4159-8ba8-e073a95e948b/image.png)
>- QuerySet이라는 자료의 형태로 감싸진 채로 표시됨
>- QuerySet이란? 
>- 데이터베이스(DB)에서 전달받은 객체 목록

<br/>
<br/>

# 객체 목록만 말고 더 자세하게 표시할 수 있게끔 수정

>![](https://velog.velcdn.com/images/97gkswn/post/e03234f5-90b3-4a1b-b7fc-1c04174b5ae4/image.png)
- 전달받은 posts를 순회하며 post에 담는것을 반복
- <django가 제공하는 기능>
- 정적인 언어인 html에  {% %} , {{ }} 와 같은 기호들을 통해 HTML 내에 동적인 구문사용가능 ( for loop, if ) 


<br/>

>-웹페이지 화면 (제목,날짜,내용이 웹페이지에 잘 나옴) 
>![](https://velog.velcdn.com/images/97gkswn/post/4ea2a4a1-e885-4c63-9957-2406632a80c4/image.png)


<br/>

## 객체들을 필터링해서 가져오는방법
(views.py)
>![](https://velog.velcdn.com/images/97gkswn/post/4effc9b4-7a07-422c-aa40-1a23e647541a/image.png)
- 날짜를 기준으로 정렬(order_by)해서 posts에 담기게됨
- '-date' = 내림차순 , 'date' =오름차순

<br/>

>-웹페이지 화면 (내림차순 : 글 목록이 최근->오래된 것 순으로 나옴)
>![](https://velog.velcdn.com/images/97gkswn/post/5b97adf9-25a6-4699-a3c0-e161e96e3f49/image.png)



<br/>
<br/>

## primary key를 지정 해 주지 않았을 때

- 테이블마다 primary key 가 존재
- primary key를 따로 지정해주지않으면 알아서 설정함
- id라는 숫자형 primary key값을 객체가 만들어진 순서로 설정
- 첫 번째 만들어진 id =1
- 두 번째 만들어진 id =2
>![](https://velog.velcdn.com/images/97gkswn/post/d0cab88c-bbca-46c7-b9f8-d5dfea289da5/image.png)

<br/>

- 웹페이지 화면
>![](https://velog.velcdn.com/images/97gkswn/post/eed9426c-349e-4236-b824-4021b21f231a/image.png)

<br/>
<br/>

- 제목,날짜,내용이 다 나오게 말고
- 제목만 나오고 제목을 누르면 나머지가 나오면 좋겠다
- 그러기 위해선 아래와 같이 URL을 만들면 됨
- 127.0.0.1:8000/detail/id (primarykey)
- 127.0.0.1:8000/detail/1
- 127.0.0.1:8000/detail/2
- 127.0.0.1:8000/detail/3

>(index.html)
>- 우선 제목을 누를 수 있도록 index.html 에서 a태그를 이용해 만듦
>![](https://velog.velcdn.com/images/97gkswn/post/c2bab89c-e29b-40b7-a6ea-1ed0550afa0f/image.png)


<br/>

>- urls.py (url눌렀을 때 어떤동작을 할지 정해야함)
>![](https://velog.velcdn.com/images/97gkswn/post/494ce792-4b9b-4f4c-bdce-213d0078bd61/image.png)
- detail/ 뒤에 정수(int)가 오면 blog_id라는 변수에 담아서 views.py에 있는 detail함수에 보내줄것이다. 라는 의미


- 결론적으로 index.html 에 있는 a태그 즉 url을 클릭하면 urls.py에 쓴것처럼 그런 url이 들어오면 detail함수로 넘어가고 detail함수는 primary key(id)까지 받아서 처리함

<br/>
<br/>

>(views.py) ( detail 함수 생성)
>- detail 함수 생성 -> html에 객체 넘겨주기 위해
>![](https://velog.velcdn.com/images/97gkswn/post/6cb69b4f-7240-484e-bb63-ec3781361fd2/image.png)
 ![](https://velog.velcdn.com/images/97gkswn/post/f7aa0c1e-d596-4e3f-9e82-af1c5425cd40/image.png)
 
<br/>
<br/>

- (detail.html)
>![](https://velog.velcdn.com/images/97gkswn/post/852cfc23-9c71-47a4-815c-f43cc0da8075/image.png)
><br/>
><br/>
- 실제 웹페이지 화면
>
>![](https://velog.velcdn.com/images/97gkswn/post/fde9303c-581f-4914-9a37-f4db675959f9/image.png)
>![](https://velog.velcdn.com/images/97gkswn/post/e1d0e308-fe23-4190-a138-4e2f4f4a3f0c/image.png)

<br/>
<br/>
<br/>

# media파일 다루기 
## media파일이란? 사용자가 업로드한 파일
- 사용자가 파일 업로드 할 수 있도록 세팅
- 1.settings.py (MEDIA_ROOT, MEDIA_URL)
- 2.urls.py 수정 (+static~)
- 3.models.py 에서 Blog객체에 photo추가
- 4.html에서 인코딩타입 추가
- 5.views.py 에서 FILES요청 받도록 추가
- 6.pillow 패키지 설치
<br/>
<br/>

>- (settings.py)
> 
>![](https://velog.velcdn.com/images/97gkswn/post/a8a52450-fe58-4aa7-b4df-8a07ccb0f0a1/image.png)
- MEDIA_Root부분->미디어 파일을 어떤 폴더에 저장 할 지 (프로젝트('BASE_DIR'렉토리) 내에 'media'라는 폴더가 자동으로 생성됨)
- MEDIA_URL부분->그 경로의 url을 정해주는 부분 (각 media 파일에 대한 URL Prefix)
- ![image](https://user-images.githubusercontent.com/103047410/175001873-a43e027a-ff39-4cee-998c-b98c56eed114.png)


<br/>

>- urls.py 
![](https://velog.velcdn.com/images/97gkswn/post/651d9e75-78b5-4fa8-8ddc-a6ef562024dd/image.png)
- 외우는게 좋다(관례적으로 쓰임)

<br/>
<br/>

>- models.py
>
>![](https://velog.velcdn.com/images/97gkswn/post/2a297a82-c27f-459d-827e-cb1cc7977834/image.png)
- Blog객체에 이미지타입의 photo변수 추가
- (blank)비어있어도 되고 NULL 이어도 된다
- 아까 베이스디렉토리 내에 생성된 media 폴더 내에 (미디어데이터가 추가될때마다) 'blog_photo'가 자동으로 생성되어 저장된다.
![](https://velog.velcdn.com/images/97gkswn/post/b7bce2d3-d44b-45a6-9486-9752cc5dbd77/image.png) 



<br/>
<br/>

>- form.create.html( html에 사용자가 파일 업로드 가능하도록 수정)
>![](https://velog.velcdn.com/images/97gkswn/post/3583506d-b1a1-480d-8266-4e046bb2debd/image.png)
- 파일을 업로드하기 위해서는 enctype(인코딩타입)을 multipart/form-data 로 바꿔줘야함

<br/>
<br/>

>- views.py
>
>![](https://velog.velcdn.com/images/97gkswn/post/c379832d-fe40-4767-b28b-9bc27aea0792/image.png)




>![](https://velog.velcdn.com/images/97gkswn/post/cc699b04-6ac8-42f8-b801-c1680ea230ef/image.png)
- 이미지 파일 다루기위해 Pillow 설치

>![](https://velog.velcdn.com/images/97gkswn/post/f7b302ef-1a22-4762-bace-c1eb6baaa1c2/image.png)
- 설치 후에 makemigrations -> migrate
- 안해주면 에러남


<br/>
<br/>

![](https://velog.velcdn.com/images/97gkswn/post/5e188c67-5c8f-4475-be75-0ec1cdf2fa7b/image.png)

![](https://velog.velcdn.com/images/97gkswn/post/ad5f55bd-83be-4615-915e-2144e1c48b7f/image.png)
>- media폴더가 생기고 그 안에 또 blog_photo폴더가 생기고 사진파일이 blog_photo 폴더 안에 저장됨 

<br/>
<br/>

>- 제목을 클릭해서 들어가면 사진까지도 나올 수 있게 detail.html을 수정
>![](https://velog.velcdn.com/images/97gkswn/post/bbc346cf-63bf-4c46-8add-5e1aebd27805/image.png)
>![](https://velog.velcdn.com/images/97gkswn/post/33a8bdfc-d14b-41ce-a9ef-476ef0f15732/image.png) 


![](https://velog.velcdn.com/images/97gkswn/post/3d87b0c3-a0ae-483d-b85e-27dd43f374f1/image.png)

 >정리 
>- DB에 있는 (Blog)객체를 html에 표현
>- 사용자가 파일 올릴 수 있도록 세팅 (Media file)
