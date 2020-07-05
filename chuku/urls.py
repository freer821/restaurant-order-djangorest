from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'chuku', UserChukuViewSet)
router.register(r'admin/chuku', AdminChukuViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]