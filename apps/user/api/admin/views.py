from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import (
    validate_password,
)
from django.core.exceptions import ValidationError

from rest_framework import generics, status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.api.admin.serializers import (
    SuperUserSerializer,
    LoginSuperUserSerializers,
    UserSerializer,
    UpdateUserSerializer,
)
from utils.paginations.page_size import PageSizeNumberPagination
from utils.permissions.superuser import IsSuperUser


User = get_user_model()


class ListCreateSuperUserView(generics.ListCreateAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = SuperUserSerializer
    queryset = User.objects.filter(is_superuser=True)
    search_fields = ['username', 'first_name', 'last_name']
    
    def create(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        password_conf = request.data.get('password_conf', '')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')

        if '' in (username, password, password_conf, first_name, last_name):
            return Response(
                {'message': 'All fields are required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if ' ' in username:
            return Response(
                {'username': 'Invalid username.'}
            )
        
        if User.objects.filter(username=username).exists():
            return Response(
                {'message': f'There ia an admin with the username {username}'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if password != password_conf:
            return Response(
                {'message': 'The passwords are not match.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            validate_password(password, User(username=username))
        except ValidationError:
            return Response(
                {'message': 'Invalid password'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_superuser(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        return Response(
            {'message': SuperUserSerializer(user).data},
            status=status.HTTP_200_OK,
        )


class RetrieveDestroySuperUserView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = SuperUserSerializer
    
    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=True).all()
        return queryset


class LoginSuperUserView(generics.CreateAPIView):
    serializer_class = LoginSuperUserSerializers

    def create(self, request, *args, **kwargs):
        username = str(request.data.get('username', '')).lower()
        password = request.data.get('password', '')

        if '' in (username, password):
            return Response(
                {'message': 'All fields are required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            user = User.objects.filter(is_superuser=True).get(username=username)
            is_correct = check_password(password, user.password)

            if is_correct:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        'refresh_token': str(refresh),
                        'access_token': str(refresh.access_token),
                        'id': user.pk,
                    },
                )
            else:
                return Response(
                    {'message': 'The username or password is incorrect.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            return Response(
                {'message': 'There is no user with this username.'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class ListUserView(generics.ListAPIView):
    permission_classes = [IsSuperUser]
    filter_backends = [SearchFilter]
    pagination_class = PageSizeNumberPagination
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False).all()
    search_fields = ['phone_number', 'email', 'first_name', 'last_name']


class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsSuperUser]
    serializer_class = UpdateUserSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False).all()
