import django_filters
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.db.models import Sum, F
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from chuku.models import Chuku
from common.utils import getRandomNo
from config.middleware import getStandardResponse
from config.permissions import IsOwner
from ruku.models import Forecast
from warehouse.models import Warehouse
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
    activate_code = request.GET.get('activecode', '')
    if len(activate_code) > 0:
        activate_user_handle(activate_code)
        return Response(getStandardResponse(200, 'user activated successfully'))

    return Response(getStandardResponse(500, 'user activated failed!'))


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard(request):
    data = {}
    if request.user.is_superuser:
        user = request.GET.get('user','')
        if user:
            data['forecast_num'] = Forecast.objects.filter(owner__id=user).aggregate(Sum('expected_num')).get(
                'expected_num__sum', '0')
            data['ruku_num'] = Forecast.objects.filter(owner__id=user).aggregate(Sum('real_num')).get(
                'real_num__sum', '0')
            data['product_good_num'] = Warehouse.objects.filter(owner__id=user).aggregate(Sum('normal_num')).get(
                'normal_num__sum', '0')
            data['product_ungood_num'] = Warehouse.objects.filter(owner__id=user).aggregate(
                product_ungood_num=Sum(F('error0_num') + F('error1_num'))).get('product_ungood_num', '0')
            data['chuku_forecast_num'] = Chuku.objects.filter(owner__id=user, sendtime__isnull=True).aggregate(
                Sum('num')).get('num__sum', '0')
            data['chuku_num'] = Chuku.objects.filter(owner__id=user, sendtime__isnull=False).aggregate(
                Sum('num')).get('num__sum', '0')
        else:
            data['forecast_num'] = Forecast.objects.all().aggregate(Sum('expected_num')).get('expected_num__sum', '0')
            data['ruku_num'] = Forecast.objects.all().aggregate(Sum('real_num')).get('real_num__sum', '0')
            data['product_good_num'] = Warehouse.objects.all().aggregate(Sum('normal_num')).get('normal_num__sum', '0')
            data['product_ungood_num'] = Warehouse.objects.all().aggregate(
                product_ungood_num=Sum(F('error0_num') + F('error1_num'))).get('product_ungood_num', '0')
            data['chuku_forecast_num'] = Chuku.objects.filter(sendtime__isnull=True).aggregate(Sum('num')).get(
                'num__sum', '0')
            data['chuku_num'] = Chuku.objects.filter(sendtime__isnull=False).aggregate(Sum('num')).get('num__sum', '0')

    else:
        data['forecast_num'] = Forecast.objects.filter(owner=request.user).aggregate(Sum('expected_num')).get('expected_num__sum', '0')
        data['ruku_num'] = Forecast.objects.filter(owner=request.user).aggregate(Sum('real_num')).get('real_num__sum', '0')
        data['product_good_num'] = Warehouse.objects.filter(owner=request.user).aggregate(Sum('normal_num')).get('normal_num__sum', '0')
        data['product_ungood_num'] = Warehouse.objects.filter(owner=request.user).aggregate(product_ungood_num= Sum(F('error0_num')+F('error1_num'))).get('product_ungood_num', '0')
        data['chuku_forecast_num'] = Chuku.objects.filter(owner=request.user, sendtime__isnull=True).aggregate(Sum('num')).get('num__sum', '0')
        data['chuku_num'] = Chuku.objects.filter(owner=request.user, sendtime__isnull=False).aggregate(Sum('num')).get('num__sum', '0')

    return Response(getStandardResponse(200, '', data))


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


class FilemanagementViewSet(viewsets.ModelViewSet):
    queryset = FileManagement.objects.all()
    serializer_class = FileManagementSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('-updatedtime')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, file=self.request.FILES.get('file'))

# ----------- Admin ---------------------
class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAdminSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return self.queryset.filter(is_superuser=False)


class AdminFilemanagementViewSet(viewsets.ModelViewSet):
    queryset = FileManagement.objects.all()
    serializer_class = AdminFileManagementSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'owner']

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')
