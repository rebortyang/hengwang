from django.contrib import admin
from .models import BlogPost, BlogBody, UserInfo
# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'get_time')

    def get_title(self, obj):
        return obj.title
    get_title.short_description = '标题'

    def get_time(self, obj):
        print(obj.timestamp)
        return '{0}年{1}月{2}日 {3}点{4}分'.format(obj.timestamp.year, obj.timestamp.month, obj.timestamp.day,
                                              obj.timestamp.hour, obj.timestamp.minute)
    get_time.short_description = '发表时间'


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'work', 'company', 'email')


class BlogBodyAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_type', 'blog_timestamp', 'blog_author')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogBody, BlogBodyAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
