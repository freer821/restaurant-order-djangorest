from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'admin/order', AdminOrderViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]