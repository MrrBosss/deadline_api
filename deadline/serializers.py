from rest_framework import serializers 
from .models import Project, Status, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
