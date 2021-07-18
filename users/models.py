from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    picture = models.ImageField(upload_to='images', null=True)
    created = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.user.username)

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=250, null=True)
    project_image = models.ImageField(upload_to='images', null=True)
    description = models.TextField(max_length=500, null=True)
    link = models.CharField(max_length=250, null=True)
    rating = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title