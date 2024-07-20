from rest_framework import serializers

from django.contrib.auth import get_user_model
from .models import Department

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'avatar')
        read_only_fields = ('username', 'email')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

