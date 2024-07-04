from rest_framework.routers import DefaultRouter
from django.urls import path
from deadline.views import ProjectViev



router = DefaultRouter()
# router.register('projects', ProjectViev, basename='projects')
urlpatterns = router.urls
urlpatterns += [
    path('projects/', ProjectViev.as_view(), name='projects'),
]