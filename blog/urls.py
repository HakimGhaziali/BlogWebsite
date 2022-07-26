from django.contrib import admin
from django.urls import path , include

from .views import post_create, post_list , post_detail

urlpatterns = [
    path('', post_list , name='post_list'),
    path('<int:pk>' , post_detail , name='post_detail'),
    path('new/' , post_create , name='post_create'),
    
]
