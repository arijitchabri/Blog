from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    blogs = Blog.objects.all().reverse()
    content = {'blogs' : blogs}
    return render(request, 'index.html', content)

def create_blog(request):
    form = BlogForm()
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
    content = { 'form' : form}
    return render(request, 'create_blog.html', content)