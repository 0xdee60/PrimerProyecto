from django import forms
from .models import Post

class PostCrear(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo','contenido')
