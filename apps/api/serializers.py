
from rest_framework import serializers
from ..users.models import Project

# create serializers
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
