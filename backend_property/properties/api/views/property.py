# Import Serializer

from rest_framework.response import Response

from backend_property.properties.api.serializers.property import PropertyModelSerializer

# Import Models
from backend_property.properties.models.property import Property
from backend_property.properties.models.typeProperty import TypeProperty
from backend_property.users.models import User

# Import Third Party Library
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class PropertyViewSet(mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      GenericViewSet):
    serializer_class = PropertyModelSerializer
    queryset = Property.objects.filter(is_active=True)
    lookup_field = 'unique_code'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def perform_destroy(self, instance):
        """Disable Entity."""
        instance.state = False
        instance.save()

    def create(self, request, *args, **kwargs):
        data = request.data

        typeProperty_obj = TypeProperty.objects.filter(unique_code=data['typeProperty']).filter()
        if typeProperty_obj:
            if typeProperty_obj[0].name == 'Urbano':
                if data.get('address') != '' and data.get('address') is not None:
                    new_property = Property.objects.create(typeProperty_id=typeProperty_obj[0].id,
                                                           identifyCatrastal=data['identifyCatrastal'],
                                                           address=data['address'],
                                                           identify=data['identify'])

                    new_property.save()

                    for users_data in data['users']:
                        users_obj = User.objects.get(unique_code=users_data['unique_code'])
                        new_property.users.add(users_obj)

                    serializer = PropertyModelSerializer(new_property)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'data': request.data, 'message': 'Please send address'},
                                    status=status.HTTP_400_BAD_REQUEST)
            elif typeProperty_obj[0].name == 'Rural':
                if data.get('name') != '' and data.get('name') is not None:
                    new_property = Property.objects.create(typeProperty_id=typeProperty_obj[0].id,
                                                           identifyCatrastal=data['identifyCatrastal'],
                                                           name=data['name'],
                                                           identify=data['identify'])

                    new_property.save()

                    for users_data in data['users']:
                        users_obj = User.objects.get(unique_code=users_data['unique_code'])
                        new_property.users.add(users_obj)

                    serializer = PropertyModelSerializer(new_property)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'data': request.data, 'message': 'Please send address'},
                                    status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, unique_code=None, *args, **kwargs):
        data = request.data
        pp = Property.objects.filter(unique_code=unique_code, is_active=True).first()
        if pp:
            for users_data in data['users']:
                users_obj = User.objects.filter(unique_code=users_data['unique_code']).first()
                if users_obj is not None:
                    for users_instance in pp.users.all():
                        if users_instance.unique_code == users_obj.unique_code:
                            return Response(data={'data': users_obj.unique_code, 'message': 'User Register in this '
                                                                                            'Property'},
                                            status=status.HTTP_406_NOT_ACCEPTABLE)
                        else:
                            pp.users.add(users_obj)
                else:
                    return Response(status=status.HTTP_204_NO_CONTENT)
            try:
                pp.save()
            except:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            propertySer = PropertyModelSerializer(pp)
            return Response(propertySer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['DELETE'], detail=True)
    def delete_users(self, request, unique_code=True):
        properties = self.get_object()
        for users_data in request.data['users']:
            users_obj = User.objects.filter(unique_code=users_data['unique_code']).first()
            if users_obj is not None:
                for users_instance in properties.users.all():
                    if users_instance.unique_code == users_obj.unique_code:
                        properties.users.remove(users_obj)
                    else:
                        return Response(data={'data': users_obj.unique_code, 'message': 'Record not Found'},
                                        status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        try:
            properties.save()
        except:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        propertySer = PropertyModelSerializer(properties)
        return Response(propertySer.data)
