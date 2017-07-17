from django.shortcuts import render
from .models import UserInfo, BlogBody
# Create your views here.


def index(request):
    user_info = UserInfo.objects.first()
    blog_body = BlogBody.objects.all()

    return render(request, 'blog/index.html', {'userInfo': user_info, 'blogBody': blog_body})


def article(request, blog_body_id=''):
    blog_body_content = BlogBody.objects.get(id=blog_body_id)
    print(blog_body_content)
    return render(request, 'blog/view.html', {'blog_body': blog_body_content})
