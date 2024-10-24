from django.shortcuts import render
from .models import Post, Tag

# Create your views here.

def blog_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog_list.html', {'posts': posts, 'tags': tags})

def homepage(request):
    return render(request, 'homepage.html')
