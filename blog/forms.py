from django import forms

from .models import BlogBody
# forms


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = BlogBody
        fields = ['blog_title', 'blog_type', 'blog_body', 'blog_imgurl', 'blog_author']
