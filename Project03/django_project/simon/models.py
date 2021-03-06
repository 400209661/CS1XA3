from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Score(models.Model):
    score = models.CharField(max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.score
