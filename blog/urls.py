from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls import url
#from django.contrib.auth.views import post_list

from .views import emailView, successView

urlpatterns = [
    path('', views.index, name='index'),
   # path('', views.post_list, name='post_list')
    url(r'^post_list/$', views.post_list, name='post_list'),
     path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('email/', views.emailView, name='email'),
    path('success/' , views.successView, name='success'),
]
