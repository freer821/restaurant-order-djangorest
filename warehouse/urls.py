from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'admin/warehouse', AdminWarehouseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]