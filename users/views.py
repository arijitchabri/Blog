from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Users
from .forms import UsersForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def users(request):
    users = Users.objects.all()
    context = {'users' : users}
    messages.info(request, f'you are {request.user}')
    return render(request, 'users/index.html', context= context) 

@login_required(login_url='login')
def create_user(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            user = User.objects.get(username = request.user)
            form.users = user
            form.save()

            subject = "Welcome to Blogbay"
            message = 'We are glad to have you here.\nEnjoy our little effort.'
            user_mail = Users.objects.get(users=request.user).mail
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user_mail],
                fail_silently=False,
            )
        return redirect('users')
    context = {'form' : form}
    return render(request, 'users/create_user.html', context)

def loginUser(request):
    page = 'login'
    context = {'page' : page}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'user not exits')
            return redirect('login')

        user = authenticate(request, username = username, password = password)
        
        if user:
            messages.success(request, 'login successfully')
            login(request, user)
            return redirect('users')
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('login')                
    return render (request, 'users/login.html', context = context)

def logoutUser(request):
    logout(request)
    messages.error(request, 'logout successfully')
    return redirect('Home')

   

def registerUser(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username = username, password = password)
            login(request, user)
            print('login successful')
            messages.error(request, 'loged in as', username)
            return redirect('create_user')
    context = {'page' : page, 'form':form}
    return render(request, 'users/login.html', context)

@login_required
def modifyUser(request, username):
    page = 'modify'
    user = User.objects.get(username = username)
    
    if not(request.user.is_superuser) and user != request.user:
        messages.error(request, 'You are not authorize to modify this account!')
        return redirect('users')
    form = UserChangeForm(instance = user)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = user)
        if form.is_valid():
            form.save()
            messages.error(request, 'Modification complete', username)
            return redirect('users')
    context = {'page' : page, 'form':form}
    return render(request, 'users/login.html', context)


@login_required
def deleteUser(request, username):
    user = User.objects.get(username = username)
    if user != request.user and not(request.user.is_superuser):
            messages.error(request, 'You are not authorize to delete this account!')
            return redirect('users')
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    return render (request, 'blog/delete_blog.html')


