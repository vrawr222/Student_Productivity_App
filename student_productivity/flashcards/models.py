from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Flashcard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    next_review = models.DateField(default=date.today)
    interval = models.IntegerField(default=1)

    def __str__(self):
        return self.question