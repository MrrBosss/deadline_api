from rest_framework.routers import DefaultRouter
from django.urls import path, include
from deadline.views import ProjectViewSet, ProcessListView, DomainViewSet



router = DefaultRouter()
router.register('domains', DomainViewSet, basename='domains')
router.register('projects', ProjectViewSet, basename='project')
# router.register('process-list', ProcessListView, basename='process-list')
urlpatterns = router.urls
urlpatterns += [
    path('process-list/', ProcessListView.as_view(), name='process-list'),
]
