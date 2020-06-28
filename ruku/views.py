import django_filters
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, pagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from config.middleware import getStandardResponse
from ruku.models import Forecast
from ruku.serializers import UserForecastSerializer


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

        super(UserForecastViewSet, self).create(request, args, kwargs)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)