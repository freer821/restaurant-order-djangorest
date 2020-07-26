import django_filters
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from common.utils import getRandomNo
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['order_no']

    def create(self, request, *args, **kwargs):
        data = request.data
        data['order_no'] = 'BL'+ getRandomNo()
        return super(OrderViewSet, self).create(request, args, kwargs)


class AdminOrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['order_no']

    def create(self, request, *args, **kwargs):
        data = request.data
        data['order_no'] = 'BL'+ getRandomNo()
        return super(OrderViewSet, self).create(request, args, kwargs)