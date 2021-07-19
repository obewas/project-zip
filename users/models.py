from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Photo(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    picture = models.ForeignKey(Photo, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    contact = models.CharField(max_length=250, null=True)
    profession = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.user.username)


class Project(models.Model):
    min= 0
    max=10
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    screenshot1 = CloudinaryField('image')
    screenshot2 = CloudinaryField('image')
    screenshot3 = CloudinaryField('image')
    screenshot4 = CloudinaryField('image')
    description = models.TextField()
    link = models.CharField(max_length=100)
    design = models.FloatField(blank=True, default=0, validators=[MinValueValidator(min), MaxValueValidator(max)],)
    usability = models.FloatField(blank=True, default=0,validators=[MinValueValidator(min), MaxValueValidator(max)],)
    creativity = models.FloatField(blank=True, default=0,validators=[MinValueValidator(min), MaxValueValidator(max)],)
    content = models.FloatField(blank=True, default=0, validators=[MinValueValidator(min), MaxValueValidator(max)],)
    overall_score = models.FloatField(blank=True, default=0,validators=[MinValueValidator(min), MaxValueValidator(max)],)
    posting_date = models.DateTimeField(auto_now_add=True,validators=[MinValueValidator(min), MaxValueValidator(max)],)

    def __str__(self):
        return self.title

    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(Q(username__username=search_term) | Q(title__icontains=search_term) | Q(overall_score__icontains=search_term))
        return projects


class Grading(models.Model):
    min = 0
    max = 10
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design = models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)
    usability = models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)
    creativity = models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)
    content = models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)
    mobile = models.FloatField(validators=[MinValueValidator(min), MaxValueValidator(max)],)

    def __str__(self):
        return str(self.project)

    def grade_total(self):
        average_grade = self.design + self.usability + self.creativity + self.content + self.mobile / 5
        return average_grade




skype_session_attendance = models.FloatField(
    validators=[MinValueValidator(min), MaxValueValidator(max)],
)