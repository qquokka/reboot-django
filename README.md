# Django

## Model 정의

* title: CharField maxlength = 30
* content: textfield
* created_at : auto_now_add, datetimefield
* updated_at : auto_now, datetimefield

## CRUD

* C
  * `/new/` :  글 작성 form
  * `/create/` : 저장 후 index로 보내기(redirect)
* R
  * `/1/` : detail 함수에서 처리
* D
  * `/1/delete/` : 삭제 후 index로 보내기
* U
  * `/1/edit/` : 글 수정 form
  * `/1/update/` : 저장 후 Read로 보내기



Static 폴더를 처음 만들었을 땐 static 안에 있는 파일들을 html에 적용시키려면 꼭 서버를 껐다 켜야 함