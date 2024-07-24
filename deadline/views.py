from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .serializers import ProjectSerializer, ListProjectSerializer, TaskSerializer, JobSerializer
from .models import Project, Status, Job
from .filters import ProjectFilter
# Create your views here.


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ListProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter


class ProjectUpdateView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDestroyView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

class TaskListView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = TaskSerializer
    

class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
  

