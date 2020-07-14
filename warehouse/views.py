import django_filters

# Create your views here.
from django.db import transaction
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from config.middleware import getStandardResponse
from warehouse.serializers import *


class AdminWarehouseViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            viewsets.GenericViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'owner']

    @action(detail=False, methods=['post'])
    def create_handle(self, request):
        current_user = int(self.request.query_params.get('current_user'))
        warehouse = Warehouse.objects.filter(owner_id=current_user, product_name=request.data.get('product_name')).first()
        if warehouse is None:
            Warehouse.objects.create(owner_id=current_user,
                                     product_name=request.data.get('product_name'),
                                     unknown_num=int(request.data.get('num')))
        else:
            warehouse.unknown_num += int(request.data.get('num'))
            warehouse.save()

        return Response(getStandardResponse(200))

    @action(detail=False, methods=['post'])
    def massiv_check_handle(self, request):
        current_user = int(request.data.get('current_user'))
        num = int(request.data.get('num'))
        product_name = request.data.get('product_name')
        status = request.data.get('status')
        warehouse = Warehouse.objects.filter(owner_id=current_user, product_name=product_name).first()
        if warehouse is None:
            return Response(getStandardResponse(400, '产品未找到，请检查录入商品名和用户名是否正确'))
        elif num > warehouse.unknown_num:
            return Response(getStandardResponse(400, '录入数量大于待操作数量，请修改数量！'))
        elif status == 'normal':
            warehouse.normal_num += num
        elif status == 'error0':
            warehouse.error0_num += num
        else:
            warehouse.error1_num += num

        warehouse.unknown_num -= num
        warehouse.save()
        return Response(getStandardResponse(200))


class AdminProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser,]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['warehouse', 'product_name', 'sn_code']

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        current_user = int(request.data.get('current_user'))
        product_name = request.data.get('product_name')
        warehouse = Warehouse.objects.filter(owner_id=current_user, product_name=product_name).first()
        if warehouse is None:
            return Response(getStandardResponse(400, '产品未找到，请检查录入商品名和用户名是否正确'))
        elif 1 > warehouse.unknown_num:
            return Response(getStandardResponse(400, '录入数量大于待操作数量，请修改数量！'))

        status = request.data.get('status')
        if status == 'normal':
            warehouse.normal_num += 1
        elif status == 'error0':
            warehouse.error0_num += 1
        else:
            warehouse.error1_num += 1

        warehouse.unknown_num -= 1
        warehouse.save()

        return super(AdminProductViewSet, self).create(request, args, kwargs)


class UserWarehouseViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name' ]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('-updatedtime')


class UserProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'sn_code']
