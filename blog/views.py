from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def index(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'blog_posts': blog_posts})
