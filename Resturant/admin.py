from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name',)
    list_filter = ('name',)
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','category')
    search_fields = ('name','category')
    list_filter = ('category','name','price')
    
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id','name','status')
    search_fields = ('name',)
    list_filter = ('status',)
    list_editable = ('status',)
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','total_price','order_status','payment_status')
    search_fields = ('user',)
    list_filter = ('created_at',)
    list_editable = ('order_status',)
    inlines = [OrderItemInline]



