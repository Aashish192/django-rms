from django_filters import rest_framework as filters
from .models import *

class FoodFilter(filters.FilterSet):
    class Meta:
        model = Food
        fields = {
            'category':['exact'],
            'price':['lt','gt']
        }
    
class TableFilter(filters.FilterSet):
    class Meta:
        model = Table
        fields = {
            'name':['exact'],
            'status':['exact']
        }

class OrderFilter(filters.FilterSet):
    class Meta:
        model = Order
        fields = {
            'user':['exact'],
            'total_price':['lt','gt'],
            'created_at':['exact']
        }

class OrderItemFilter(filters.FilterSet):
    class Meta:
        model = OrderItem
        fields = {
            'food':['exact'],
            'quantity':['lt','gt'],
            'price':['lt','gt'],
            'created_at':['exact']
        }