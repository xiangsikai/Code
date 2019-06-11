"""s14day19_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from app01 import views


"""
urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^index/(\d+)/', views.index,name='indexx'),
    url(r'^index/(?P<nid>\d+)/', views.index,name='indexx'),
    path('login/', views.login),
    # path('home/', views.home),
    path('home/', views.Home.as_view()),
    url(r'^detail/', views.detail),
    # 返回一个值,d+也可以写为w+任意正则
    url(r'^detai-(?P<nid>\d+).html', views.detail),
    # 返回多个值
    #url(r'^detail-(\d+)-(\d+).html', views.detail),
    # 返回多个值并指定变量赋值
    #url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
]
"""

urlpatterns = [
    # 指定分发的app目录名称
    url(r'^cmdb/',include("app01.urls")),
    url(r'^monitor/',include("app02.urls")),
]
























