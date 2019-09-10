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

Model명은 무조건 단수로 해야 함! 예를 들어, Articles -> Article

다른 사람 코드 고칠 때 :

1. 다른사람 리포에서 내 리포로 Fork
2. Fork한 저장소를 clone하기
3. 직접 코드 수정
   * add, commit
4. fork한 저장소로 push
5. 내 github에서 fork된 리포로 들어가서 pull request 보내기



클래스명 : CamelCase

함수명과 변수명: snake_case

최대한 많은 것들을 재사용 가능하게 하자!

App은 복수형을 쓰고,  Class는 단수형을 쓴다.



css 변경사항이 적용 안 될 땐 브라우저에서 *캐시 비우기 및 강력 새로고침* 한다.

(개발자 도구가 떠있는 상태에서 새로고침에 우클릭하면 나옴)



html은 태그나 속성 등에 대해 대소문자 구분을 하지 않지만 views.py는 파이썬 파일이라 명령어, 변수 등에 대해 대소문자를 구분함. views.py에서는 POST를 무조건 대문자로 써야 하므로 html에서도 그냥 대문자로 써줌



GET으로 요청 보낼 때 url 맨 뒤에 `/`를 안 붙여도 Django가 알아서 `/` 붙여서 보내줌. 그래서 요청을 두 번 보내게 됨!

POST는 `/` 붙이는 걸 못 해줌