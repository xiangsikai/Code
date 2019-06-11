from django.contrib import admin
from django.conf.urls import url,include
from app01 import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^index', views.index),
    url(r'^user_info', views.user_info),
    url(r'^userdetail-(?P<nid>\d+)/', views.user_detail),
    #url(r'^user_group', views.user_group),
    url(r'^orm/', views.orm),
]

