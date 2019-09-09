from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]

# 1. urlpatterns라는 변수 필요
# 2. 함수를 연결시켜주기 위해 path 필요
# 3. viewsㅇ 안에 있는 함수를 가져오기 위해 views 필요