from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
# [myApp/models.py](myApp/models.py)
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class User(models.Model):  # Note: Using capital letter for class names is Python convention
    first_name = models.CharField(max_length=100, required=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True, required=True)
    password = models.CharField(max_length=100, required=True)  # Note: In production, never store raw passwords
    created_at = models.DateTimeField(auto_now_add=True, required=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

  
class Blog(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
  date_created = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return f"{self.title} by {self.author}"