from django.shortcuts import render

# Create your views here.
def allposts(request):
    return render(request, 'blog/allposts.html')
