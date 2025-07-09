from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

user = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='food_images/', null=True, blank=True) 
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Table(models.Model):
    STATUS_CHOICE = [
        ("A", "available"),
        ("N", "not available"),
    ]

    name = models.CharField(max_length=3)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="A")

class Order(models.Model):
    ORDER_STATUS = [
        ("P", "pending"),
        ("C", "completed"),
    ]

    PAYMENT_STATUS = [
        ("P", "paid"),
        ("U", "unpaid"),
    ]

    user = models.ForeignKey(user, on_delete=models.CASCADE)
    total_price = models.FloatField()
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS, default="P")
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    food = models.ForeignKey(Food, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
