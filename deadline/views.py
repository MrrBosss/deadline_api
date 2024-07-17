from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets

from .serializers import ProjectSerializer, ProcessSerializer, DomainSerializer, ProjectCreateSerializer,\
      DeveloperSerializer
from .models import Project, Process, Domain, Developer
from .filters import ProjectFilter
# Create your views here.


class ProjectViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProjectFilter


class ProcessListView(generics.ListAPIView):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    http_method_names = ['get']


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    http_method_names = ['post']


class ProjectCreateApiView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ['get']
    pagination_class = None