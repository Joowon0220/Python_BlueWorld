from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
#     프로젝트의 urls 에서 넘어온 url 값이 ''(공백)이면 views.py의 index 라는 함수로 가라

]