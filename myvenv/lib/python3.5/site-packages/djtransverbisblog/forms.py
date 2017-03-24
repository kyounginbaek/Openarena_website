from django import forms
from .models import Post, Comment, Page


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'email_address', 'text',)


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ('title', 'en_content', 'page_order', 'sidebar')