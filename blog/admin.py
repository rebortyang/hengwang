from django.contrib import admin
from .models import BlogPost
# Register your models here.
from datetime import datetime


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_time')

    def get_title(self, obj):
        return obj.title
    get_title.short_description = '标题'

    def get_time(self,obj):
        print(obj.timestamp)
        return '{0}年{1}月{2}日 {3}点{4}分'.format(obj.timestamp.year, obj.timestamp.month, obj.timestamp.day,
                                              obj.timestamp.hour, obj.timestamp.minute)
    get_time.short_description = '发表时间'

admin.site.register(BlogPost, BlogPostAdmin)