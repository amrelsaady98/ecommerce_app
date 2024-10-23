from django.template.context_processors import request
from django.urls import path

from authentication import views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', views.login, name='token_obtain_pair'),
]