from django.db import models
from django.utils import timezone


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField('标题', max_length=200)
    body = models.TextField('内容')
    timestamp = models.DateTimeField('发表时间', auto_now_add=True)

    def __str__(self):
        return self.title
