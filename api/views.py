from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateCategory(generics.CreateAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class GetCategory(generics.ListAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer2(category, many=True)
        return Response({"category": serializer.data})
