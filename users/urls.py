from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name = 'users'),
    path('create_user', views.create_user, name = 'create_user'),
    path('login', views.loginUser, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
]
