from django.shortcuts import render
from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Project
# Create your views here.



class ProjectViev(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']
    