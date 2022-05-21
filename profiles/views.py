from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import ListView, DetailView


class ProfileDetailView(DetailView):
    template_name = "profiles/detail.html"
    model = User
    context_object_name = 'user'
    http_method_names = ['get']
    slug_field = 'username'
    slug_url_kwarg = 'username'