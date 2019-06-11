from django.contrib import admin
from django.conf.urls import url,include
from app02 import views



urlpatterns = [
    url(r'^login/', views.login),
]