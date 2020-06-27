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

#    def list(self, request, *args, **kwargs):
#        pagination.PageNumberPagination.page_size = self.request.query_params.get('limit', 20)



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)