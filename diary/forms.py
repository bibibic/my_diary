from django import forms
from .models import Add_story

from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Add_story
        fields = ('title', 'content', 'image')
