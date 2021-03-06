"""alien URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from quiz.models import *
from django.shortcuts import get_object_or_404, render, redirect
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('quiz', views.quiz, name='quiz'),
    path('result/', views.result, name='result'),
    path('result/rock', views.rock, name='rock'),
    path('result/raccoon', views.raccoon, name='raccoon'),
    path('result/martian', views.martian, name='martian'),
    path('result/baby', views.baby, name='baby'),
    path('result/president', views.president, name='president'),
    path('result/wizard', views.wizard, name='wizard'),
    path('result/dog', views.dog, name='dog'),
    path('DIS', views.DIS, name='DIS'),



    # path('reset/', views.reset, name='reset'),

    # 재형's 기존 코드
    # path('addScore/<int:score>', views.addScore, name='addScore'),

]