from django.db import models
from django.contrib.auth.nodels import User
# Create your models here.
class Score(models.Model):
    score = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
