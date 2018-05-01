"""apocrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('for_students', views.for_students, name='for_students'),
    path('summer_schools', views.summer_schools, name='summer_schools'),
    path('clubs', views.clubs, name='clubs'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('news/<int:news_id>', views.read_news, name='read_news'),
    path('projects', views.projects, name='projects'),
]
