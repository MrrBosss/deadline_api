from django.urls import path
from .views import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDestroyView

urlpatterns = [
    path('project-list', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('new/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('<int:pk>/delete/', ProjectDestroyView.as_view(), name='project_delete'),
]
