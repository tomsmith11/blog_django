from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(max_length=200, unique=True)
  password = models.CharField(max_length=100)
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.email
  
class Blog(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"{self.title} by {self.author}"