# Import Third party
from rest_framework import serializers

# Import Model
from backend_property.properties.models.typeProperty import TypeProperty


class TypePropertyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeProperty
        fields = '__all__'

    def to_representation(self, instance):
        super().to_representation(instance)
        return {
            'unique_code': instance.unique_code,
            'description': instance.description,
            'name': instance.name
        }