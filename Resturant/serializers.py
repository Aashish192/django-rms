from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer): # ✅ singular
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # id = serializers.IntegerField(read_only = True)
    
    # def create(self,validated_data):
    #     return Category.objects.create(**validated_data)
    class Meta:
        model = Category
        fields = '__all__'
    
    
class FoodSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # description = serializers.CharField()
    # price = serializers.CharField()
    # category = serializers.CharField()
    
    # def create(self,validated_data):
    #     return Food.objects.create(**validated_data)

    # def update(self,instance,validated_data):   
    #     instance.name =validated_data.get('name',instance.name)
    #     instance.save()
    #     return instance
    class Meta:
        model = Food
        fields = '__all__'
    

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
    
class OrderItemSerializer(serializers.Serializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class AdminDashboardSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    total_orders = serializers.IntegerField()
    total_revenue = serializers.DecimalField(max_digits=10, decimal_places=2)
        
