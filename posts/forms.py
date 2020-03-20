from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    model = forms.Form
    fields = ['title', 'content', 'genre', 'post_author']

    class Meta:
        model = Post
        fields = ['title', 'content', 'genre', 'post_author']
