from django.shortcuts import render ,get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.decorators import api_view  # ✅ Correct import for api_view
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import Category,Food,OrderItem,Table,Order
from .serializers import CategorySerializer,FoodSerializer,TableSerializer,OrderItemSerializer,OrderSerializer,AdminDashboardSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from .permission import IsWorkerOrAdminOrReadOnly, IsWorkerOrAdmin, IsWorkerOrIsAdminOrPostOnly,IsAdmin
from rest_framework import filters
from .filters import FoodFilter,TableFilter,OrderFilter,OrderItemFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum
from django.contrib.auth import get_user_model
# Create your views here.

class CategroyApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination	
    permission_classes = [IsWorkerOrAdminOrReadOnly]
    
class FoodApiView(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination	
    permission_classes = [IsWorkerOrAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = FoodFilter
    
class TableApiView(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsWorkerOrAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = TableFilter
    
class OrderApiView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsWorkerOrIsAdminOrPostOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = OrderFilter

class OrderItemApiView(ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsWorkerOrIsAdminOrPostOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = OrderItemFilter

class AdminDashboardViewSet(ViewSet):
    permission_classes = [IsAdmin]

    def list(self, request):
        User = get_user_model()
        total_users = User.objects.count()
        total_orders = Order.objects.count()
        total_revenue = Order.objects.filter(order_status='C').aggregate(total=Sum('total_price'))['total'] or 0

        data = {
            "total_users": total_users,
            "total_orders": total_orders,
            "total_revenue": total_revenue,
        }
        serializer = AdminDashboardSerializer(data)
        return Response(serializer.data)