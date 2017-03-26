from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class httpdata(models.Model):
    ip = models.CharField(max_length=500, verbose_name='ip')
    title = models.CharField(max_length=500, verbose_name='title')
    header = models.TextField(verbose_name='header')


    def __str__(self):
        return self.title
