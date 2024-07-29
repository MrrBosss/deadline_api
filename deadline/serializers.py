from rest_framework import serializers 
from django.contrib.auth import get_user_model

from .models import Project, Status, Job


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name", "avatar", "is_superuser")
        model = User


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


class ListProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    job = JobSerializer(many=True)
    status = TaskSerializer(many=False)
    class Meta:
        model = Project
        fields = '__all__'