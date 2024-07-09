from django.shortcuts import render
from rest_framework import generics, mixins, viewsets
from .serializers import ProjectSerializer, ProcessSerializer, DomainSerializer
from .models import Project, Process, Domain
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



class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    http_method_names = ['post']