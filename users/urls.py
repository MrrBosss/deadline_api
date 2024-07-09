
from django.urls import path
from .views import MyTokenObtainPairView, MyTokenRefreshView, UserRetrieveUpdateAPIView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserRetrieveUpdateAPIView.as_view(), name='user-me'),
    # Other URLs for your views
]