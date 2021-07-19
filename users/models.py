from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
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
    profession = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.user.username)


class Project(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    screenshot2 = models.ImageField(upload_to='images')
    screenshot3 = models.ImageField(upload_to='images')
    screenshot4 = models.ImageField(upload_to='images')
    description = models.TextField()
    link = models.CharField(max_length=100)
    design = models.FloatField(blank=True, default=0)
    usability = models.FloatField(blank=True, default=0)
    creativity = models.FloatField(blank=True, default=0)
    content = models.FloatField(blank=True, default=0)
    overall_score = models.FloatField(blank=True, default=0)
    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(overall_score__icontains=search_term))
        return projects


class Grading(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.FloatField()
    usability = models.FloatField()
    creativity = models.FloatField()
    content = models.FloatField()
    mobile = models.FloatField()

    def __str__(self):
        return str(self.project)

    def grade_total(self):
        average_grade = self.design + self.usability + self.creativity + self.content + self.mobile / 5
        return average_grade

