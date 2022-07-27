from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from django.urls import reverse
STATUS= (
    (0, 'Draft'),
    (1,'Publish')
)


class Post(models.Model):


    title= models.CharField(max_length=40)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status= models.IntegerField(choices=STATUS , default=0)

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args = [ self.id ])
    
