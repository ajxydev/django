from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    
    USER = models.ForeignKey(User, on_delete=models.CASCADE)


    name = models.CharField(max_length=100)

    email = models.CharField(max_length=20)

    phone = models.CharField(max_length=15)

    place = models.CharField(max_length=100)


class Blog(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)

    image = models.FileField(upload_to='blog_images/')

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


