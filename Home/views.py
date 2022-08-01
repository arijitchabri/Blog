from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    blogs = Blog.objects.all().reverse()
    content = {'blogs' : blogs}
    return render(request, 'blog/index.html', content)


@login_required(login_url='login')
def create_blog(request):
    form = BlogForm()
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    content = { 'form' : form}
    return render(request, 'blog/create_blog.html', content)

@login_required(login_url='login')
def update_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    form = BlogForm(instance = blog)
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('Home')
    content = {'form' : form}
    return render(request, 'blog/create_blog.html', content)

@login_required(login_url='login')
def delete_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('Home')

    return render(request, 'blog/delete_blog.html')