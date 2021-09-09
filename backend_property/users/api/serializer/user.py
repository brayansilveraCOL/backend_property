from django.contrib.auth import password_validation
from django.contrib.auth.models import update_last_login
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenBackendError

# locals Imports
from backend_property.users.models import User
from backend_property.users.models.typeUsers import TypeUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.email
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['email'] = str(self.user.email)
        data['username'] = str(self.user.username)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    default_error_messages = {
        'bad_token': 'Token is Expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh_token']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenBackendError:
            self.fail('Bad Token')


class SignUpSerializer(serializers.Serializer):
    typeUser = serializers.PrimaryKeyRelatedField(queryset=TypeUser.objects.filter(is_active=True))
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    identify = serializers.CharField(max_length=255, validators=[UniqueValidator(queryset=User.objects.all())])
    # Phone Number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex],
                                         max_length=17)

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, validated_data):
        data = validated_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        user.save()
        return user


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        print(instance.typeUser)
        if instance.typeUser is None:
            return {
                'unique_code': instance.unique_code,
                'identify': instance.identify,
                'email': instance.email,
                'phone_number': instance.phone_number,
                'full_name': "{} {}".format(instance.first_name, instance.last_name)
            }
        else:
            return {
                'unique_code': instance.unique_code,
                'identify': instance.identify,
                'email': instance.email,
                'typeUser': instance.typeUser.name,
                'phone_number': instance.phone_number,
                'full_name': "{} {}".format(instance.first_name, instance.last_name)
            }
