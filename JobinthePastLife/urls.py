from django.urls import path
from . import views

app_name = 'JobinthePastLife'

urlpatterns= [
    path('', views.index, name='index')
]