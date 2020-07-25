import django_filters
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from goods.models import Good, Category, FileManagement
from goods.serializers import GoodSerializer, CategorySerializer, FileManagementSerializer


class AdminGoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']


class UserGoodViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']


class AdminCategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']


class UserCategoryViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']


class AdminFilemanagementViewSet(viewsets.ModelViewSet):
    queryset = FileManagement.objects.all()
    serializer_class = FileManagementSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']

    def pre_save(self, obj):
        obj.file = self.request.FILES.get('file')
