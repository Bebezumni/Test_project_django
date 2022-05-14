from pyexpat import model
from django.views.generic import ListView, DetailView
from requests import post
from django.views.generic.edit import CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin


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


class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    success_url = '/'

    # get access to request in createview
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    # DB Needs author
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
        
    

    