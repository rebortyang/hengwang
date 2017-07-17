from django.shortcuts import render
from .models import UserInfo, BlogBody
# Create your views here.
from django.views.generic import ListView, DetailView
from django.utils import timezone


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