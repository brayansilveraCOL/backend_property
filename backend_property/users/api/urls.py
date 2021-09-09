from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view.user import MyTokenObtainPairView, LogoutApiView, UserSignupView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'signup', UserSignupView, basename='user-signup')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutApiView.as_view(), name='token_logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]