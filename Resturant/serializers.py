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
    
