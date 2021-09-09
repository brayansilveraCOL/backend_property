from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .view.user import MyTokenObtainPairView, LogoutApiView, UserSignupView, UserView
from .view.typeUser import TypeUserViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'signup', UserSignupView, basename='user-signup')
router.register(r'typeUser', TypeUserViewSet, basename='typeUser'),
router.register(r'user', UserView, basename='user'),



urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutApiView.as_view(), name='token_logout'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]