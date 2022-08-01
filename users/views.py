from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Users
from .forms import UsersForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def loginUser(request):
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
            return redirect('Home')
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('login')                
    return render (request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'logout successfully')
    return redirect('Home')

def users(request):
    users = Users.objects.all()
    context = {'users' : users}
    return render(request, 'users/index.html', context= context)

@login_required(login_url='login')
def create_user(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('users/')
    context = {'form' : form}
    return render(request, 'users/create_user.html', context)    