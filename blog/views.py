from django.shortcuts import render, redirect
from django.http import JsonResponse
# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView

from django.utils import timezone
from datetime import datetime

from .models import UserInfo, BlogBody
from .forms import AddArticleForm
from  .common import TodayOnHistory

import time

# def index(request):
#     user_info = UserInfo.objects.first()
#     blog_body = BlogBody.objects.all()
#
#     return render(request, 'blog/index.html', {'userInfo': user_info, 'blogBody': blog_body})


# def article(request, blog_body_id=''):
#     blog_body_content = BlogBody.objects.get(id=blog_body_id)
#     print(blog_body_content)
#     return render(request, 'blog/view.html', {'blog_body': blog_body_content})

# 使用Django提供的Generic display views来实现展示文章
    # 首页展示文章列表，使用ListView
    # 文章详情显示，使用DetailView


class ArticleListView(ListView):
    model = BlogBody
    context_object_name = 'blogBody'
    template_name = 'blog/index.html'

    # 不使用getXXX方法，就是默认返回model指定的数据
    # 使用getXXX方法，可以添加额外的数据
    def get_context_data(self, **kwargs):
        # 调用父类方法，返回model指定的数据
        content = super(ArticleListView, self).get_context_data(**kwargs)
        # 添加额外数据
        content['now'] = timezone.now()
        content['userInfo'] = UserInfo.objects.first()
        # content 是一个dict，里面有model指定的数据，还有你额外添加的数据，可以通过键名来访问数据；
        # 如：访问model指定的数据， blogBody - 这是你上面指定的名字，未指定的需要通过object_list；额外数据则根据键名now、userInfo获取
        return content


class ArticleDetailView(DetailView):
    model = BlogBody
    context_object_name = 'blog_body'
    template_name = 'blog/view.html'

    def get_context_data(self, **kwargs):
        # 获取数据的方法：1）URL 指定返回pk；2）URL 指定返回slug(需要在模型里面加入slug_field);

        # 根据传入的数据在model里查询结果
        content = super(ArticleDetailView, self).get_context_data(**kwargs)
        # 加入额外数据
        content['now'] = timezone.now()
        # content 是一个dict，里面有model指定的数据，还有你额外添加的数据，可以通过键名来访问数据；
        # 如：访问model指定的数据， blog_body - 这是你上面指定的名字,没指定的话通过object访问；额外数据则根据键名now、userInfo
        return content


# 文章列表
def post_of_love(request):
    love_list = BlogBody.objects.filter(blog_type='love')

    return render(request, 'blog/list.html', {'love_lists': love_list})


# 增加文章
def add_article(request):
    # return render(request, 'blog/add_article.html')
    add_form = AddArticleForm().as_p()
    return render(request, 'blog/add_article.html', {'form': add_form})


def sub_article(request):
    # if request.method == 'GET':
    #     mytype = request.GET['article_type']
    #     title = request.GET['article_title']
    #     body = request.GET['article_editor']
    #     updb = BlogBody(blog_title=title, blog_body=body, blog_type=mytype,
    #                     blog_timestamp=time.strftime("%Y-%m-%d %X", time.localtime()), blog_author='rebortyang')
    #     updb.save()
    #     return redirect('post_of_love')
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data['blog_title']
            blog_type = form.cleaned_data['blog_type']
            blog_body = form.cleaned_data['blog_body']
            blog_imgurl = form.cleaned_data['blog_imgurl']
            blog_author = form.cleaned_data['blog_author']
            blog_timestamp = timezone.now()

            blog_article = BlogBody(blog_title=blog_title, blog_type=blog_type, blog_body=blog_body,
                     blog_imgurl=blog_imgurl, blog_author=blog_author, blog_timestamp=blog_timestamp)
            blog_article.save()
            return redirect('post_of_love')
    else:
        return redirect('add_article')


def del_article(request, blog_body_id):
    BlogBody.objects.get(pk=blog_body_id).delete()

    return redirect('home')


class ArticleUpdateView(UpdateView):
    model = BlogBody
    fields = ['blog_title', 'blog_body', 'blog_type', 'blog_imgurl', 'blog_author']
    template_name = 'blog/edit_article.html'

    def get_context_data(self, **kwargs):
        content = super(ArticleUpdateView, self).get_context_data(**kwargs)

        content['up_article_id'] = self.object.id

        return content


def upadte_submit_article(request, up_article_id):
    if request.method == 'POST':
        form = AddArticleForm(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data['blog_title']
            blog_type = form.cleaned_data['blog_type']
            blog_body = form.cleaned_data['blog_body']
            blog_imgurl = form.cleaned_data['blog_imgurl']
            blog_author = form.cleaned_data['blog_author']

            update_article = BlogBody.objects.filter(pk=up_article_id)

            update_article.update(blog_title=blog_title, blog_type=blog_type,
                                  blog_body=blog_body,blog_imgurl=blog_imgurl, blog_author=blog_author)

            return redirect('/article/{0}/'.format(up_article_id,))


def today_on_history(request):
    his = TodayOnHistory()

    return JsonResponse(his.get_history(), safe=False)
