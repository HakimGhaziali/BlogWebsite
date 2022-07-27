from django.contrib import admin
from django.urls import path , include
from .views import SignUpview

urlpatterns = [
    path('/',SignUpview.as_view() , name='signup' ),
]
