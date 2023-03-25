from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from users.models import Users
from django.contrib import messages

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
        user = Users.objects.get(users = request.user)
        if form.is_valid():
            blogform = form.save(commit=False)
            blogform.author = user
            blogform.save()
            return redirect('Home')
    content = { 'form' : form}
    return render(request, 'blog/create_blog.html', content)

@login_required(login_url='login')
def update_blog(request, pk):
    blog = Blog.objects.get(id = pk)
    form = BlogForm(instance = blog)
    user = Users.objects.get(users=request.user)
    if blog.author == user:
        pass
    else:
        messages.error(request, "You can't edit this blog")
        return redirect('Home')
    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog) 
        if form.is_valid():
            blogform = form.save(commit=False)
            user = Users.objects.get(users=request.user)
            blogform.author = user
            blogform.save()
            return redirect('Home')
    content = {'form' : form}
    return render(request, 'blog/create_blog.html', content)

@login_required(login_url='login')
def delete_blog(request, pk):
    user = Users.objects.get(users=request.user)
    blog = Blog.objects.get(id = pk)
    if blog.author == user:
        pass
    else:
        messages.error(request, "You can't delete this blog")
        return redirect('Home')
    if request.method == 'POST':
        blog.delete()
        return redirect('Home')

    return render(request, 'blog/delete_blog.html')
