from .models import *
from django.forms import ModelForm

class BlogForm(ModelForm):
    
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['author',]
