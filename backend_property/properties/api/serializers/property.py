from backend_property.properties.models.property import Property
from backend_property.properties.models.typeProperty import TypeProperty
from rest_framework import serializers

from backend_property.users.api.serializer.user import UserModelSerializer


class PropertyModelSerializer(serializers.ModelSerializer):
    typeProperty = serializers.PrimaryKeyRelatedField(queryset=TypeProperty.objects.filter(is_active=True))
    users = UserModelSerializer(many=True)

    class Meta:
        model = Property
        fields = '__all__'
