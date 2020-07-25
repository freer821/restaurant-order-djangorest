from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'admin/category', AdminCategoryViewSet)
router.register(r'category', UserCategoryViewSet)
router.register(r'admin/good', AdminGoodViewSet)
router.register(r'good', UserGoodViewSet)
router.register(r'admin/store', AdminFilemanagementViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]