from django.shortcuts import render ,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.decorators import api_view  # ✅ Correct import for api_view
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet
from .models import Category,Food,OrderItem
from .serializers import CategorySerializer,FoodSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .permission import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters import rest_framework as filter

# Create your views here.

class CategroyApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class FoodApiView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination	
    filter_backends = []
    filterset_fields = ['category']  # filter by category id
    search_fields = ['name', 'category__name'] 