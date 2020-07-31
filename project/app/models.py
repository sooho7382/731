from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    grade = models.CharField(max_length=20)
    major = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,default='')
    image = models.ImageField(upload_to='images/', blank=True)

