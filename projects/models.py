from django.db import models
from users.models import Project, Profile

# Create your models here.

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


   	


