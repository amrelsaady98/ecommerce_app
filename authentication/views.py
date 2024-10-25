from venv import logger

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers, status

from authentication.models import User
from authentication.serializers import MyTokenObtainSerializer, LoginSerializer, UserSerializer, RegisterSerializer
from core.utils import api_response


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


@api_view(['POST'])
@permission_classes((AllowAny,))
def get_token(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            if user.check_password(serializer.validated_data['password']):
                refresh = RefreshToken.for_user(user)
                return api_response(
                    success=True,
                    message='Login successful',
                    data={
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': UserSerializer(user).data,},
                    status_code=status.HTTP_200_OK
                )
            else:
                return api_response(
                    success=False,
                    message='Password is incorrect',
                    status_code=status.HTTP_401_UNAUTHORIZED
                )
        except User.DoesNotExist:
            return api_response(
                success=False,
                message='User does not exist',
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # Optional: log the exception for debugging
            logger.error(f"Login error: {str(e)}")
            return api_response(
                success=False,
                message='An error occurred during login',
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    else:
        return api_response(
            success=False,
            message='Invalid input',
            data=serializer.errors,
            status_code=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes((AllowAny,))
def register_customer_api(request):
    try:
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email__iexact=serializer.validated_data['email']).exists():
                return api_response(
                    success=False,
                    message='User already exists',
                    status_code=status.HTTP_400_BAD_REQUEST
                )
            else:
                user = User.objects.create_customer(
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password'],
                    first_name=serializer.validated_data['name'].split(' ')[0],
                    last_name=serializer.validated_data['name'].split(' ')[-1],
                )
                refresh = RefreshToken.for_user(user)

                return api_response(
                    success=True,
                    message='User Registered successfully',
                    status_code=status.HTTP_201_CREATED,
                    data={
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': UserSerializer(user).data,
                    },
                )
        else:
            return api_response(
                success=False,
                message='Invalid input',
                status_code=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        # Optional: log the exception for debugging
        logger.error(f"Login error: {str(e)}")
        return api_response(
            success=False,
            message='An error occurred during login',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )