from rest_framework import serializers 
from django.contrib.auth import get_user_model
from .models import Project, Process



User = get_user_model()



class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'