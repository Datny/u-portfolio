from django.shortcuts import render
from .models import Blog
# Create your views here.


def allposts(request):
    posts = Blog.objects
    return render(request, 'blog/allposts.html', {'posts': posts})
