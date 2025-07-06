from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register('category',CategroyApiView)
router.register('food',FoodApiView)
urlpatterns = router.urls

