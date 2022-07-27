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
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    content = { 'form' : form}
    return render(request, 'create_blog.html', content)

def update_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    form = BlogForm(instance = blog)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('Home')
    content = {'form' : form}
    return render(request, 'create_blog.html', content)

def delete_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('Home')

    return render(request, 'delete_blog.html')