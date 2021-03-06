from django.db import models
from django.utils import timezone


class Joke(models.Model):
    id = models.CharField(blank=False,max_length=200,primary_key=True)
    title = models.TextField(blank=False,max_length=200,default='joke')
    joke = models.TextField(blank=False,max_length=200)
    data_posted = models.DateTimeField(default=timezone.now)

class Ips(models.Model):
    title = models.TextField(blank=False,default='the ip',max_length=200)
    ip = models.TextField(blank=False,max_length=60)
    data_posted = models.DateTimeField(default=timezone.now)
