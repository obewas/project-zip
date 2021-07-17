from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=250)
	project_image = models.ImageField(upload_to='images', null=True)
	description = models.TextField(max_length=500, null=True)
	link = models.CharField(max_length=250, null=True)
	rating = models.FloatField()

   