from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.serializers import (
    UserSerializer,
    LoginUserSerializer,
    ChangeAvatarSerializer,
    ChangeProfileSerializer,
)
from utils.message.sms_message import send_sms
from utils.message.email_message import send_email


User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):

        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        phone_number = request.data.get('phone_number', '')
        email = request.data.get('email', '')

        emails = list(map(lambda email: email.replace('.', '') if email else None, User.objects.values_list('email', flat=True)))

        if '' in (first_name, last_name):
            return Response(
                {'message': 'Fist name and Last name is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not phone_number:
            return Response(
                {'message': 'Phone number is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not phone_number.startswith('+'):
            return Response(
                {'message': 'Country code is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not phone_number.startswith('+98') and not email:
            return Response(
                {'message': 'Email is required for users outside of iran.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if str(email).replace('.', '') in emails:
            return Response(
                {'message': 'User with this email allredy exist.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if phone_number.startswith('+98'):
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save() # user = test
            # send_sms(receptor=phone_number)

            # Just for test:
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    'message': 'User successfully created.',
                    'note': 'We have sent a verification code to your phone number.',
                    'refresh': str(refresh),    # Just for test
                    'access': str(refresh.access_token),    # Just for test
                },
                status=status.HTTP_201_CREATED,
            )
        
        
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Just for test:
        refresh = RefreshToken.for_user(user)

        send_email(request=request, user=user)
        return Response(
            {
                'message': 'User successfully created.',
                'note': 'We have sent a verification link to your email.',
                'refresh': str(refresh),    # Just for test
                'access': str(refresh.access_token),    # Just for test
            },
            status=status.HTTP_201_CREATED,
        )


class UserLoginSendMessageView(generics.CreateAPIView):
    serializer_class = LoginUserSerializer

    def create(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number', '')
        email = request.data.get('email', '')

        if not phone_number:
            return Response(
                {'message': 'Phone number is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if not phone_number.startswith('+'):
            return Response(
                {'message': 'Country code is required.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        if not phone_number.startswith('+98') and not email:
            return Response(
                {'message': 'Email is required for users outside of iran.'}
            )
        
        if phone_number.startswith('+98'):
            try:
                user = User.objects.get(phone_number=phone_number)
                print(user)
                if user:
                    # send_sms(receptor=phone_number)

                    # Just for test:
                    refresh = RefreshToken.for_user(user)
                    return Response(
                        {
                            'refresh': str(refresh),    # Just for test
                            'access': str(refresh.access_token),    # Just for test
                        },
                        status=status.HTTP_201_CREATED,
                    )

            except:
                return Response(
                    {'message': 'There is no user with the given phone number.',},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if not phone_number.startswith('+98') and email:
            user = User.objects.get(email=email)
            if user:
                send_email(request=request, user=user)

                # Just for test:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        'refresh': str(refresh),    # Just for test
                        'access': str(refresh.access_token),    # Just for test
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {'message': 'There is no user with the given email.'},
                    status=status.HTTP_400_BAD_REQUEST,
                )


class UserProfileView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(instance=user)
        return Response(serializer.data)


class ChangeAvatarView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangeAvatarSerializer

    def update(self, request, *args, **kwargs):
        avatar = request.data.get('avatar', '')
        user = self.request.user

        if not avatar:
            return Response(
                {'message': 'Avatar field is empty.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ChangeAvatarSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'message': 'Avatar changed successfully.'},
            status=status.HTTP_200_OK,
        )


class ChangeProfileView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangeProfileSerializer

    def update(self, request, *args, **kwargs):
        data = request.data.copy()

        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        user = self.request.user

        if '' in (first_name, last_name):
            return Response(
                {'message': 'First name and Last name field is empty.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if user.region == 'INSIDE' and not email:
            return Response(
                {'message': 'Email field is empty.'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            data['email'] = user.email

        serializer = ChangeProfileSerializer(instance=user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        message = 'First name and Last name changed successfully.'
        if user.region == 'INSIDE':
            message = 'First name, Last name and Email changed successfully.'
        return Response(
            {'message': message},
            status=status.HTTP_200_OK,
        )
