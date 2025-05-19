# Django imports
from django.shortcuts import render
from django.contrib.auth.models import User

# DRF imports
from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import AllowAny

# Serializers imports
from .serializers import (

    RegisterSerializer

)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]