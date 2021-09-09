# Import Serializer
from backend_property.users.api.serializer.typeUser import TypeUserModelSerializer

# Import Models
from backend_property.users.models.typeUsers import TypeUser

# Import Third Party Library
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated


class TypeUserViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.CreateModelMixin,
                      GenericViewSet):
    serializer_class = TypeUserModelSerializer
    queryset = TypeUser.objects.filter(is_active=True)
    lookup_field = 'unique_code'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Entity."""
        instance.state = False
        instance.save()
