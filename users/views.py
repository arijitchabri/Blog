from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Users
from .forms import UsersForm

# Create your views here.

def users(request):
    users = Users.objects.all()
    context = {'users' : users}
    return render(request, 'users/index.html', context= context)


def create_user(request):
    form = UsersForm()
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('users/')
    context = {'form' : form}
    return render(request, 'users/create_user.html', context)    