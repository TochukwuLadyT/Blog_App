from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

