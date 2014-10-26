from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    user = models.ForeignKey(User)
