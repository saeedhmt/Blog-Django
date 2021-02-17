from django import forms
from django.forms import modelformset_factory

from .models import *


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'text', 'image', 'active']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']



class TagModelForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']


TagModelFormset = modelformset_factory(Tag, fields=('name',), extra=1, can_delete=True)

