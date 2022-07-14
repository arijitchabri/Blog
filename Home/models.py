from django.db import models

# Create your models here.

class Tags(models.Model):
    tag = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.id}  {self.tag}'


class Blog(models.Model):
    title = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    tags = models.ManyToManyField('Tags')
    description = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.id} {self.title}'