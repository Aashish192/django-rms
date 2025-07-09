from django.urls import path
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()

router.register('category',CategroyApiView)
router.register('food',FoodApiView)
router.register('table',TableApiView)
router.register('order',OrderApiView)
router.register('orderitem',OrderItemApiView)
router.register('admin/dashboard',AdminDashboardViewSet,basename='admin-dashboard')
urlpatterns = router.urls

