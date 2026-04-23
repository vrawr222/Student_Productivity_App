from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True) #instead of CASCADE use SET_NULL. null and blank = true for it veing okay if this field is not filled. best to keep it true when testing and customize later.
  title=models.CharField(max_length=200)
  description=models.TextField(null=True, blank=True)
  complete=models.BooleanField(default=False)
  create=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
  class Meta:
    ordering=['complete']
