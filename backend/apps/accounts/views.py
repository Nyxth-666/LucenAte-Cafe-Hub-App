from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from . serializers import BusinessOwnerRegistrationSerializer

class BusinessOwnerRegistrationView(generics.CreateAPIView):
    serializer_class = BusinessOwnerRegistrationSerializer
    permission_classes = [AllowAny]
