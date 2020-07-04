from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'admin/warehouse', AdminWarehouseViewSet)
router.register(r'admin/warehousedetail', AdminWarehouseDetailViewSet)
router.register(r'warehouse', UserWarehouseViewSet)
router.register(r'warehousedetail', UserWarehouseDetailViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]