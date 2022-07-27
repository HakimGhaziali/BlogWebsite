from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
from django.urls import reverse , reverse_lazy
from django.views import generic

class PostList(generic.ListView):

    model = Post 
    template_name = 'blog/post_list.html'
    context_object_name = 'post_list' 

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreate(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_new_post.html'

class PostUpdate(generic.UpdateView):
    model = Post 
    form_class = PostForm 
    template_name = 'blog/post_new_post.html'

class PostDelete(generic.DeleteView):

    model=Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')