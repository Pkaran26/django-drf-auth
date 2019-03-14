from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['pk']

class CategorySerializer2(serializers.Serializer):
    name = serializers.CharField(max_length=25)
