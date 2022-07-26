from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import PostForm
# Create your views here.
from django.urls import reverse

def post_list(request):

    post_list = Post.objects.filter(status=1)
    return render(request , 'blog/post_list.html' , {'post_list': post_list})


def post_detail(request , pk):

    post= get_object_or_404(Post , pk=pk)
    return render(request ,  'blog/post_detail.html', { 'post': post})



def post_create(request):

    form = PostForm

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()          
            return redirect(reverse('post_list'))
            
           


    else:
        form = PostForm()
        
    return render(request , 'blog/post_new_post.html' , {'form': form })
        #form = PostForm


    



