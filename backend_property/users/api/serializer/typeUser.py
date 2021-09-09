# Import Third party
from rest_framework import serializers

# Import Model
from backend_property.users.models.typeUsers import TypeUser


class TypeUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeUser
        fields = '__all__'
