from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.allposts ,name="allposts"),
    path('<int:blog_id>/', views.post_detail, name="postdetail"),

]

