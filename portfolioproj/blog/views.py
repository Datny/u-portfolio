from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def allposts(request):
    posts = Blog.objects
    return render(request, 'blog/allposts.html', {'posts': posts})

def post_detail(request,blog_id):
    detailed_post = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {"post": detailed_post})
