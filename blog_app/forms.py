from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "author"]
