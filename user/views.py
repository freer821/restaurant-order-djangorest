import django_filters
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from common.utils import getRandomNo
from config.middleware import getStandardResponse
from .serializers import *
from .services import sendNewPassw, activate_user_handle


@api_view(['POST'])
def register(request):
    data = JSONParser().parse(request)
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(getStandardResponse(200))

    return Response(getStandardResponse(500, serializer.errors))


@api_view(['POST'])
def login(request):
    username = request.data.get("username", "")
    password = request.data.get("password", "")

    user = authenticate(username=username, password=password)
    if not user:
        return Response(getStandardResponse(400, 'username or password wrong!'))

    token, _ = Token.objects.get_or_create(user=user)
    update_last_login(None, user)

    return Response(getStandardResponse(200,'', {'token': token.key}))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response(getStandardResponse(200, 'logout sucess'))


@api_view(["POST"])
def resetpassword(request):
    username = request.data.get("username", "")
    user = User.objects.filter(username=username).first()
    if user is None:
        return Response(getStandardResponse(400, "User "+username+" not found!"))

    new_pass = getRandomNo()
    user.set_password(new_pass)
    if not user.is_active:
        user.is_active = True

    user.save()

    sendNewPassw(username, new_pass)

    return Response(getStandardResponse(200, 'password changed'))


@api_view(["GET"])
def activateuser(request):
    activate_code = request.GET.get('activate_code', '')
    if len(activate_code) > 0:
        activate_user_handle(activate_code)
        return Response(getStandardResponse(200, 'user activated successfully'))

    return Response(getStandardResponse(200, 'failed!'))


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = UserRetrieveUpdateSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.get_object().check_password(serializer.data.get("oldPassword")):
                return Response(getStandardResponse(400, 'old password wrong'))
            # set_password also hashes the password that the user will get
            self.get_object().set_password(serializer.data.get("newPassword"))
            self.get_object().save()
            return Response(getStandardResponse(200, 'password changed'))

        return Response(getStandardResponse(500, serializer.errors))



# ----------- Admin ---------------------
class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username']

    def get_queryset(self):
        return self.queryset.filter(is_superuser=False)
