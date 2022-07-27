from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.auth.forms import UserCreationForm  
from django.urls import reverse_lazy


class SignUpview(generic.CreateView):

    form_class= UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')