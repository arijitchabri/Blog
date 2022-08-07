from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name = 'users'),
    path('create_user', views.create_user, name = 'create_user'),
    path('login', views.loginUser, name = 'login'),
    path('logout', views.logoutUser, name = 'logout'),
    path('register', views.registerUser, name = 'register'),
    path('modify/<str:username>', views.modifyUser, name = 'modify'),
    path('delete/<str:username>', views.deleteUser, name = 'delete')
]
