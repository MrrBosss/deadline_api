from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, viewsets
from .serializers import ProjectSerializer, ProcessSerializer, DomainSerializer, ProjectCreateSerializer
from .models import Project, Process, Domain
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
  