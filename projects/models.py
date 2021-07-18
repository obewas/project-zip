from django.db import models
from users.models import Profile

# Create your models here.
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
   		review_total = design + usability + creativity + content + mobile
   		return review_total


   	


