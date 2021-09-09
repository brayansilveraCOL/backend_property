from django.urls import path
from .view.user import MyTokenObtainPairView, LogoutApiView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutApiView.as_view(), name='token_logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]