from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend_property.properties.api.views.typeProperty import TypePropertyViewSet
from backend_property.properties.api.views.property import PropertyViewSet


router = DefaultRouter()
router.register(r'typeProperty', TypePropertyViewSet, basename='type-property')
router.register(r'property', PropertyViewSet, basename='property')



urlpatterns = [
    path('', include(router.urls))
]
