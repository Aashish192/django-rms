# user_auth/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField  # ✅ Correct import

class User(AbstractUser):   
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('worker', 'Worker'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    
    phone_number = PhoneNumberField(null=True, blank=True, default='')