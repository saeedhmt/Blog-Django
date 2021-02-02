from django import forms
from .models import *


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'text', 'image', 'tag']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']