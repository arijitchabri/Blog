from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    blogs = Blog.objects.all().reverse()
    content = {'blogs' : blogs}
    return render(request, 'index.html', content)