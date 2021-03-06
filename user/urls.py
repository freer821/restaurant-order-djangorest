from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r'admin/users', UserAdminViewSet)

urlpatterns = [
    path('regist', register),
    path('login', login),
    path('logout', logout),
    path('resetpassword', resetpassword),
    path('activateuser', activateuser),
    path('dashboard', dashboard),

    path('user/profile', UserRetrieveUpdateView.as_view()),
    path('user/changepassword', ChangePasswordView.as_view()),

    url(r'^', include(router.urls))
]