from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'admin/warehouse', AdminWarehouseViewSet)
router.register(r'admin/product', AdminProductViewSet)
router.register(r'warehouse', UserWarehouseViewSet)
router.register(r'product', UserProductViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]