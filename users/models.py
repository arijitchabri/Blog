from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length= 100)
    mail = models.EmailField(max_length= 500)
    profile_picture = models.ImageField(blank = True, null = True)
    about = models.TextField(blank=True, null = True)

    def __str__(self):
        return f'{self.id}__{self.name}'