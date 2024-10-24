from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers, status

from authentication.models import User
from authentication.serializers import MyTokenObtainSerializer
from core.utils import api_response


# Create your views here.
# login user
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainSerializer


@api_view(['POST', 'GET'])
@permission_classes((AllowAny,))
def login(request):
    try:
        user = User.objects.get(email=request.data['email'])
        refresh = RefreshToken.for_user(user)
        return api_response(
            success=True,
            message='login successful',
            data={
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data},
            status_code=status.HTTP_200_OK
        )
    except User.DoesNotExist:
        return Response({
            'error': 'User does not exist'
        })


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
