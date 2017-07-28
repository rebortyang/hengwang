"""hengwang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.index, name='home'),
    # url(r'^article/(?P<blog_body_id>[0-9]+)/$', views.article, name='article'),
    url(r'^$', views.ArticleListView.as_view(), name='home'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(), name='article'),
    url(r'^love/$', views.post_of_love, name='post_of_love'),
    url(r'^add_article/$',views.add_article, name='add_article'),
    url(r'^sub_article/$',views.sub_article, name='sub_article'),
    url(r'^del_article/(?P<blog_body_id>[0-9]+)/$', views.del_article, name='del_article'),
    url(r'^edit_article/(?P<pk>[0-9]+)/$', views.ArticleUpdateView.as_view(), name='edit_article'),
    url(r'^up_sub_article/(?P<up_article_id>[0-9]+)/$', views.upadte_submit_article, name='up_sub_article'),
    url(r'^today_on_history/$', views.today_on_history, name='today_on_history'),
]
