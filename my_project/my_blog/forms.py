from django import forms
from .models import *

class blogForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['author_name','comment']

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['heading','content']
        