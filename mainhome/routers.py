from rest_framework.routers import DefaultRouter
from django.urls import path, include

from deadline.views import TaskListView, JobListView
from users.views import DepartmentListView


router = DefaultRouter()
urlpatterns = router.urls
urlpatterns += [
    path('jobs', JobListView.as_view(), name='jobs'),
    path('departments/', DepartmentListView.as_view(), name='departments'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('users/', include('users.urls')),
    path('project/', include('deadline.urls')),
]
