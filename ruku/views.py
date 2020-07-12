import json

import django_filters

# Create your views here.
from django.utils import timezone
from rest_framework import generics, viewsets, pagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from config.middleware import getStandardResponse
from ruku.models import Forecast
from ruku.serializers import UserForecastSerializer, AdminForecastSerializer
from warehouse.apps import addWareIntoWarehous


class UserForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = UserForecastSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'logistic_code']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('-updatedtime')

    def create(self, request, *args, **kwargs):
        data = request.data
        forecast = self.get_queryset().filter(logistic_code=data['logistic_code'], product_name=data['product_name']).first()
        if forecast is not None:
            return Response(getStandardResponse(300, '%s and %s already exits' % (data['logistic_code'], data['product_name'] )))

        return super(UserForecastViewSet, self).create(request, args, kwargs)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdminForecastViewSet(viewsets.ModelViewSet):
    queryset = Forecast.objects.all()
    serializer_class = AdminForecastSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'logistic_code', 'owner']

    @action(detail=False, methods=['post'])
    def ruku_handle(self, request):
        current_user = int(self.request.query_params.get('current_user'))
        data = request.data
        forecast = Forecast.objects.filter(owner_id=current_user, product_name=request.data.get('product_name'),
                                           logistic_code=request.data.get('logistic_code')).first()
        if forecast is not None:
            forecast.real_num = int(data.get('real_num'))
            forecast.admin_extra=json.dumps(data.get('admin_extra'))
            forecast.arrivedtime=timezone.now()
            forecast.save()
            addWareIntoWarehous(current_user, forecast.product_name, forecast.real_num)
            return Response(getStandardResponse(200))
        return Response(getStandardResponse(400, 'forecast not found!'))
