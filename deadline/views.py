from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .serializers import ProjectSerializer, ProcessSerializer
from .models import Project, Process
# Create your views here.



class ProjectViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



class ProcessListView(generics.ListAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    http_method_names = ['get']