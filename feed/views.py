from pyexpat import model
from django.views.generic import ListView, DetailView
from requests import post

from .models import Post

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-id')[0:30]
    
    
class PostDetailView(DetailView):
    template_name = "feed/detail.html"
    model = Post
    context_object_name = 'post'
    http_method_names = ['get']
    