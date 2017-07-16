from django.db import models
from django.utils import timezone


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField('标题', max_length=200)
    body = models.TextField('内容')
    timestamp = models.DateTimeField('发表时间', auto_now_add=True)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    nickname = models.CharField('网名', max_length=20)
    work = models.CharField('职业', max_length=20)
    company = models.CharField('公司', max_length=50)
    email = models.EmailField('电子邮箱')

    def __str__(self):
        return self.nickname


class BlogBody(models.Model):
    blog_title = models.CharField('文章标题', max_length=50)
    blog_body = models.TextField('文章内容')
    blog_type = models.CharField('文章类型', max_length=50)
    blog_timestamp = models.DateTimeField('时间')
    blog_imgurl = models.CharField('图片', max_length=50, null=True)
    blog_author = models.CharField('作者', max_length=20)
