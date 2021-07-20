from django.contrib import admin
from .models import Profile, Project, Grading, Photo

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Grading)
admin.site.register(Photo)