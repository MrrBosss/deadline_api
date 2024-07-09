import django_filters
from .models import Project
# filters.py



class ProjectFilter(django_filters.FilterSet):
    developer_name = django_filters.CharFilter(field_name='developer_name', lookup_expr='icontains')
    start_day = django_filters.DateFilter(field_name='start_day', lookup_expr='gte')
    end_day = django_filters.DateFilter(field_name='end_day', lookup_expr='lte')

    class Meta:
        model = Project
        fields = ['developer_name', 'start_day', 'end_day']
