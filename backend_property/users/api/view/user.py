from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, mixins, viewsets

from backend_property.users.api.serializer.user import MyTokenObtainPairSerializer, LogoutSerializer, SignUpSerializer, UserModelSerializer
from backend_property.users.models import User


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LogoutApiView(GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSignupView(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    """
       Class Signup to Create User
       """

    def create(self, request, *args, **kwargs):
        """
        function create to User
        :param request:
        :param args:
        :param kwargs:
        :return: Response Object
        """
        if request:
            serializer = SignUpSerializer(data=request.data)
            serializer_data = serializer.is_valid(raise_exception=True)
            user = serializer.save()
            data = UserModelSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(mixins.ListModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = UserModelSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'unique_code'
    queryset = User.objects.filter(is_active=True)

