## 댓글 구현하기
---
# Foreign Key
>외래키(Foreign Key)란 테이블의 필드 중에서 다른 테이블의 행과 식별할 수 있는 키를 의미함<br/>
>즉, 테이블과 테이블을 연결하기 위해 사용되는 키임
>
>만약 외래키를 사용하지 않고 게시물과 댓글의 내용을 저장할 기능을 구현한다면 다음과 같은 테이블로 생성해야 함<br/>
>![1](/1.png)<br/>
>위 형태는 하나의 테이블에 너무 많은 열이 추가되어 효율적이지 못한 구조가 됨<br/>
>
>다음과 같이 두 테이블로 나눌 수 있음
>![2](/2.png)<br/>
>Comment 테이블을 별도로 생성하고 해당 내용이 어느 Post 테이블의 id에서 사용되었는지 표기하면(외래키) 간단하게 효율적인 테이블을 구성할 수 있다
---

1. Comment Model 만들기
    - **blogapp의 models.py**
    ```
        class Comment(models.Model):
            comment = models.Charfield(max_length=200)          #댓글(최대 길이 200자 제한)
            date = models.DateTimeField(auto_now_add=True)      #작성 날짜(생성 날짜 자동 저장)
            post = models.ForeignKey(Blog, on_delete=CASCADE)   #blog 개체를 참조하는 foreign key
            #on_delete=CASCADE은 참조하는 대상이 삭제되면 자신도 삭제하라는 옵션
    ```
    Comment 테이블을 생성
    Comment 테이블의 comment, date, post(외래키) 필드를 정의함

    class ForeignKey ( to , on_delete , **options )
    외래키를 작성할 때 필수적으로 포함되어야 할 매개변수에는 참조할 테이블과 개체 삭제 시 수행할 동작(on_delete)이 있다.


    - **blogapp의 admin.py**
    ![3](/admin_register_comment.png)<br/>
    ```
        admin.site.register(Comment)	#admin 사이트에 등록
    ```

    - **blogapp의 models.py 내 class Comment** 
    ![4](/model_notstr.png)![5](/model_str.png)<br/>
    ```
        def __str__(self):
            return self.comment		
            #admin 화면에서 comment를 반환하도록 수정. 데이터베이스 자체를 변경하는 것은 아니므로 migration 필요 없음
    ```

2. Form 만들기
    - **blogapp의 forms.py**
    ```
        from .models import Comment	#models.py에서 만든 Comment 가져오기
        class CommentForm(form.ModelForm):	
        #Django의 forms.ModelForm으로부터 상속받기
            class Meta:
                model = Comment
                fields = [‘comment’]	#comment를 입력 받을 것
    ```

    - **blogapp의 views.py**
    ```
        def detail(request, blog_id):	#detail 페이지에서 댓글 폼 찍기
            comment_form = CommentForm()
        return render(request, ~~~ {‘comment_form’:comment_form})
    ```

    - **blogapp templates 폴더 내 detail.html**

    ![5](/detailpage.png)<br/>
    ```
        <form>method=”Post” action=”{% url ‘create_comment’ blog_detail.id %}”>
        #제출 버튼을 누르면 create_comment url로 이동, 어떤 블로그 글인지 알 수 있는 blog_detail.id도 함께 보냄. 
        #id값은 어떤 글인지 특정지을 수 있는 django의 primary key
            {% csrf_token %}
            {{ comment_form }}
            <input type=”submit”>	#제출 버튼
        </form>				#form을 만들어줌
    ```

    - **장고 프로젝트 내 url.py**
    ```
        path(‘create_comment/<int:blog_id>’, views.create_comment, name=’create_comment’),
    ```
    #어떤 게시글에서 저장되었는지 알 수 있도록 <int:blog_id>를 views.creaet_comment에 인자로 전달

    - **blogapp의 views.py**
    ```
        def create_comment(request, blog_id):
            filled_form = CommentForm(request.POST)				#filled_form변수에 CommentForm으로부터 request.POST 형식으로 받아온 데이터를 넣음

            if filled_form.is_valid():		#filled_form이 제대로 입력되었다면
                finished_form = filled_form.save(commit=False)		#아직 저장하지는 말고 finished_form에 담음
                finished_form.post = get_object_or_404(Blog, pk=blog_id)	  #그 객체의 post에 Blog 중 pk값이 blog_id인 것을 담음
            finished_form.save()
            return redirect(‘detail’, blog_id) #이 blog_id값을 갖고 있는 detail 페이지로 이동
    ```

    - **detail.html 에 댓글 목록들 표시**

    ![6](/comment_set.png)<br/>
    ```
        {% for comment in blog_detail.comment_set.all %} 
        #특정 객체 blog_detail을 참조하는 comment 모델의 집합 blog_detail.comment_set 을 모두 가져오기 위해 .all
        <p> {{ comment }} </p>
        {% endfor %}
    ```

<br/><br/><br/>

## 로그인/로그아웃
---
# django.contrib.auth를 통해 Django authentication system 사용하기
User 개체가 인증 시스템의 핵심이다. 일반적으로 사이트와 상호작용하는 사람들을 나타내며, 접근 제한, 사용자 등록, 작성자와 콘텐츠의 연결 등과 같은 작업을 하는 데 사용됨

User 개체는 username, password, email, first_name, last_name 등의 속성을 가짐

# 사용자 인증
authenticate()를 통해 사용자인지를 확인한다. 인자로 username, password 등을 받아 그것이 유효하다면 User object를 반환한다. 아니라면 None을 반환한다

#_로그인과 로그아웃
Django의 django.contrib.auth 앱을 이용해 구현할 수 있다.

```
django.contrib.auth.login(request, user, backend=None)
```
request 객체와 user객체를 통해 로그인한다.
backend 옵션을 통해 이메일 형식의 아이디 입력, 일반 단어 형식의 아이디 입력, 소셜 로그인 등으로 로그인하도록 로그인 방식을 변경할 수 있다.

```
django.contrib.auth.logout(request)
```

---

- **터미널에서 python manage.py startapp accounts**
    #로그인/로그아웃 기능 담당하는 새로운 app accounts 만들기
    settings.py의 INSTALLED_APPS에 accounts 등록하기

- **index.html 에**
    ```
        <a href="{% url 'login' %}">로그인</a>
    ```

- **urls.py에 url 연결하기**
    ```
    from accounts import views as accounts_views    #as는 다른 이름으로 쓰겠다는 것
        urlpatterns = [
            ...
            path('login/', accounts_views.login, name='login'),
            # login이라는 url이 주어졌을 때 accounts_views 안에 있는 login이라는 함수가 실행됨. 해당 url에 login이라는 별칭 부여
        ]
    ```

- **account의 views.py에 login 만들기**
    ```
        def login(request):
            #POST 요청이 들어오면 로그인 처리를 해줌
            if request.method == ‘POST’:
                pass
            else:
                return render(request, ‘login.html’)
                #GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할을 함
    ```

- **login.html 만들기**

    ![7](/loginpage.png)<br/>
    ```
    <form action=”{% url ‘login’ %}” method=”POST”>
        {% csrf_token %}
        username : <input type=’text’ name=”username”><br/>
        password : <input type=’password’ name=’password’>
        <br/>
        <input type=”submit” value=”로그인”>
    </form>
    ```

- **account의 views.py**
    ```
    from django.contrib import auth
    from django.contrib.auth.models import User	#Django에 내장된 User객체
        def login(request):
            #POST 요청이 들어오면 로그인 처리를 해줌
            if request.method == ‘POST’:
                userid = request.POST[‘username’]	#username을 담아줌
                pwd = request.POST[‘password’]
                user = auth.authenticate(request, username=userid, password=pwd)
            #데이터베이스에 저장된 회원인지의 여부를 판별하는 내장 기능
            #이미 저장되어 있는 회원이라면 user객체를 반환하고 아니면 none을 반환함
                if user is not None:
                    auth.login(request, user)
                    return redirect(‘home’)
                else:
                    return render(request, ‘login.html’)
            #GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할을 함
            else:
                    return render(request, ‘login.html’)
        
        def logout(request):
            auth.logout(request)
            return redirect('home')
    ```

- **index.html**

    ![8](/login.png)<br/>
    ![9](/notlogin.png)<br/>

    ```
    {% if user.is_authenticated %}	        #로그인이 된 상태
    안녕하세요. {{ user.username }}님?<br/>
    <a href=”{% url ‘logout’ %}”>로그아웃</a>
    {% else %}			                    #로그인이 안된 상태
    아직 로그인이 되지 않았습니다.<a href=”{% url ‘login’ %}”>로그인</a>
    {% endif %}
    <br/>
    ```

- **settings.py**
    ```
    LOGIN_REDIRECT_URL=”/”
    #로그인이 성공했을 경우 home으로 redirect하도록 함
    ```