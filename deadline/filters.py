
import django_filters
from django_filters import rest_framework as filters
from .models import Project
from users.models import Department

class ProjectFilter(filters.FilterSet):
    user = django_filters.CharFilter(field_name='user__name', lookup_expr='icontains')
    completed_after = filters.DateFilter(field_name='end_day', lookup_expr='gte')
    completed_before = filters.DateFilter(field_name='end_day', lookup_expr='lte')
    department = filters.ModelChoiceFilter(field_name="user__department", queryset=Department.objects.all()
    )
    order_by = filters.OrderingFilter(
        fields=(
            ('start_day', 'start_day'),
            ('end_day', 'end_day'),
            ('created_at', 'created_at'),
        ),
        field_labels={
            'start_day': 'Start Day',
            'end_day': 'End Day',
            'created_at': 'Creation Date',
        },
        label="Order by"
    )

    class Meta:
        model = Project
        fields = ['user', 'department','completed_after', 'completed_before']






