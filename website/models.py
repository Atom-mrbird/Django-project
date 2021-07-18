from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return  self.title
class Content(models.Model):
        name = models.CharField(blank=False,max_length=100)
        data_posted = models.DateTimeField(default=timezone.now)
        id = models.IntegerField(primary_key=True)
        def __str__(self):
            return self.name