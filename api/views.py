from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated

class CreateCategory(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GetCategory(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
