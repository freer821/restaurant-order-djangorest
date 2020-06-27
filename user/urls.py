from django.urls import path

from .views import *

urlpatterns = [
    path('regist', register),
    path('login', login),
    path('logout', logout),
    path('resetpassword', resetpassword),
    path('activateuser', activateuser),

    path('user/profile', UserRetrieveUpdateView.as_view()),
    path('user/changepassword', ChangePasswordView.as_view()),

]