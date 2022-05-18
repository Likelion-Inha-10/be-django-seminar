## 백엔드 장고 세션 세번째 세미나 안내



### 📝 **학습목표**

URL Mapping에 대해 알 수 있다.

Static에 대해 알 수 있으며, Static 자원들을 사용할 수 있다.

Template 언어와 Bootstrap을 이용할 수 있다.

RDB(Relational DataBase)를 알고, Model을 구성할 수 있다.

HTML Form을 이용하여 사용자 입력을 받을 수 있고 QuerySet을 이용하여 Detail Page를 구현할 수 있다.

Media 기능을 활용하여 File Upload를 구현할 수 있다.

Foreign Key를 이용하여 댓글 기능을 구현할 수 있다.

django auth를 이용하여 로그인/로그아웃 기능을 구현할 수 있다.



### 📅 **일정 안내**

**5/25 (수) 오후 7시 오프라인** **(장소 미정)**



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
- 만약 **`2주차 수요일(세션 1) 김예은-이혜윤`** 페어라고 가정하였을 때 **브랜치명**은 `02-01-김예은-이혜윤`으로 작성
- _**브랜치명을 반드시 준수할 것**_
- **_절대로, 어떠한 일이 있어도, 다른 페어의 파일을 수정하지 말 것. 자신의 페어 폴더만 수정하고 변경할 것._**
- **과제는 이미 생성되어 있는 2주차 수요일 (세션 1) 폴더에 있는 페어 폴더 안쪽**에 자유롭게 제출 후 PR 생성
- 브랜치 생성 방법과 PR 방법은 [이곳](https://github.com/Likelion-Inha-10/be-assignments-submit-practice/blob/main/README.md) 을 참조


### 🦁 페어 안내

- **김예은-이혜윤**
- **이민성-정민경**
- **이한주-김홍진**
- **정승찬-정여진**



### 🏆 학습 범위

> ⚠️ **주의**
>
> Django Document에서의 학습 내용은 일단 만드는 **Django에서 언급한 키워드나 내용을 위주로 심화 학습**하도록 합니다. 그 이상 학습하는 것도 굉장히 좋은 학습 방식일 수 있으나, **여러분의 학업스트레스와 분노로 인해 파손된 전자기기는 책임질 수 없습니다.** 더불어 공식 문서의 한국어 번역 퀄리티가 좋지 않습니다. 되도록 **영어로 보시는게 정신 건강에 이롭습니다.**

- **김예은-이혜윤**
  - 일단 만드는 Django
    - Chapter3 [Project1] 회사 소개 사이트
      - url mapping 1 ~ template 상속
  - [Django Document](https://docs.djangoproject.com/en/4.0/)
    - [URLconfs](https://docs.djangoproject.com/en/4.0/topics/http/urls/)
    - [How to manage static files (e.g. images, JavaScript, CSS)](https://docs.djangoproject.com/en/4.0/howto/static-files/#how-to-manage-static-files-e-g-images-javascript-css)
    - [The Django template language](https://docs.djangoproject.com/en/4.0/ref/templates/language/#the-django-template-language)

- **이민성-정민경**
  - 일단 만드는 Django
    - Chapter4 [Project2-1] 개발자 대나무숲 프로젝트 준비하기
      - CRUD, 완성형 서비스로! ~ 사용자 입력받기 - modelForm
  - [Django Document](https://docs.djangoproject.com/en/4.0/)
    - [The model layer의 Models 부분](https://docs.djangoproject.com/en/4.0/#the-model-layer)
    - [Forms](https://docs.djangoproject.com/en/4.0/#forms)

- **이한주-김홍진**
  - 일단 만드는 Django
    - Chapter4 [Project2-1] 개발자 대나무숲 프로젝트 준비하기
      - QuerySet ~ File Upload - Media 2
  - [Django Document](https://docs.djangoproject.com/en/4.0/)
    - [The model layer의 QuerySets 부분](https://docs.djangoproject.com/en/4.0/#the-model-layer)
    - [The view layer의 File uploads 부분](https://docs.djangoproject.com/en/4.0/#the-view-layer)

- **정승찬-정여진**
  - 일단 만드는 Django
    - Chapter4 [Project2-1] 개발자 대나무숲 프로젝트 준비하기
      - 댓글 구현하기1 ~ 로그인/로그아웃 3
  - [Django Document](https://docs.djangoproject.com/en/4.0/)
    - [Relationship fields](https://docs.djangoproject.com/en/4.0/ref/models/fields/#module-django.db.models.fields.related)
    - [Relationships](https://docs.djangoproject.com/en/4.0/topics/db/models/#relationships)
    - [Common web application tools의 Authenticatoin 부분](https://docs.djangoproject.com/en/4.0/#common-web-application-tools)