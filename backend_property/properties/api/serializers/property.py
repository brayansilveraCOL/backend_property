from backend_property.properties.models.property import Property
from rest_framework import serializers

from backend_property.users.api.serializer.user import UserModelSerializer
from backend_property.properties.api.serializers.typeProperty import TypePropertyModelSerializer


class PropertyModelSerializer(serializers.ModelSerializer):
    users = UserModelSerializer(read_only=True, many=True)
    typeProperty = TypePropertyModelSerializer(read_only=True)

    class Meta:
        model = Property
        fields = ['unique_code', 'identify', 'typeProperty', 'identifyCatrastal', 'address', 'name', 'users']
