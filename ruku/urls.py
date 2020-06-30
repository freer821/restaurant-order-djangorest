from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'forecasts', UserForecastViewSet)
router.register(r'admin/forecasts', AdminForecastViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]