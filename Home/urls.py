from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='Home'),
    path('create_blog', views.create_blog, name='create_blog'),
]
