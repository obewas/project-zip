from rest_framework import serializers
from .models import Project, Profile
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):

	class Meta:
		model = Project
		fields = ['profile', 'title', 'project_image', 'description', 'link', 'rating']



class ProfileSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())

    class Meta:
        model = Profile
        fields = ['id', 'username', 'projects']


