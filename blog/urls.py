from django.contrib import admin
from django.urls import path , include

from .views import PostCreate, PostList , PostDetail , PostUpdate , PostDelete

urlpatterns = [
    path('', PostList.as_view() , name='post_list'),
    path('<int:pk>' , PostDetail.as_view() , name='post_detail'),
    path('new/' , PostCreate.as_view() , name='post_create'),
    path('<int:pk>/update' , PostUpdate.as_view() , name='post_update'),
    path('<int:pk>/delete' , PostDelete.as_view() , name='post_delete'),
    
]
