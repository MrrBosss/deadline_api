from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets

from .serializers import ProjectSerializer, TaskSerializer, JobSerializer
from .models import Project, Status, Job
from .filters import ProjectFilter
# Create your views here.


class JobListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # http_method_names = ['get']


class ProjectViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter


class TaskListView(generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = TaskSerializer
    # http_method_names = ['get']


