from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.admin import *


class Post(models.Model):
    title = models.TextField(max_length=200)
    content = models.TextField(blank=False,max_length=200)
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return  self.title
class Content(models.Model):
        name = models.TextField("type",blank=True,max_length=200)
        data_posted = models.DateTimeField(default=timezone.now)
        def __str__(self):
            return self.name