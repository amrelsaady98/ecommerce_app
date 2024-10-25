from django.template.context_processors import request
from django.urls import path

from authentication import views

urlpatterns = [
    path('token/', views.get_token, name='token_obtain_pair'),
    path('register-customer/', views.register_customer_api, name='register_customer'),
]