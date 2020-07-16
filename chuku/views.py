import django_filters
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chuku.apps import statusChangedChuku
from chuku.models import Chuku
from chuku.serializers import UserChukuSerializer, AdminChukuSerializer
from config.middleware import getStandardResponse
from warehouse.models import Warehouse


class UserChukuViewSet(viewsets.ModelViewSet):
    queryset = Chuku.objects.all()
    serializer_class = UserChukuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'logistic_code']

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user).order_by('-updatedtime')

    def create(self, request, *args, **kwargs):
        warehouse = Warehouse.objects.filter(owner=self.request.user, product_name=request.data.get('product_name')).first()
        if warehouse is None:
            return Response(getStandardResponse(400, '产品未找到，请检查录入商品名是否正确'))
        return super(UserChukuViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, status='created')

    def update(self, request, *args, **kwargs):
        warehouse = Warehouse.objects.filter(owner=self.request.user, product_name=request.data.get('product_name')).first()
        if warehouse is None:
            return Response(getStandardResponse(400, '产品未找到，请检查录入商品名是否正确'))

        return super(UserChukuViewSet, self).update(request, args, kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status != 'created':
            return Response(getStandardResponse(400, '已处理中，不能删除，请联系管理员'))

        return super(UserChukuViewSet, self).destroy(request, args, kwargs)
        
        
class AdminChukuViewSet(viewsets.ModelViewSet):
    queryset = Chuku.objects.all()
    serializer_class = AdminChukuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['product_name', 'owner', 'logistic_code']

    def create(self, request, *args, **kwargs):
        current_user = int(request.data.get('owner'))
        warehouse = Warehouse.objects.filter(owner_id=current_user, product_name=request.data.get('product_name')).first()
        if warehouse is None:
            return Response(getStandardResponse(400, '产品未找到，请检查录入商品名和用户名是否正确'))
        return super(AdminChukuViewSet, self).create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        current_user = int(request.data.get('owner'))
        warehouse = Warehouse.objects.filter(owner_id=current_user, product_name=request.data.get('product_name')).first()
        if warehouse is None:
            return Response(getStandardResponse(400, '产品未找到，请检查录入商品名和用户名是否正确'))

        status = request.data.get('status')
        if status == 'finished':
            request.data['sendtime'] = timezone.now()
            statusChangedChuku(self.get_object(), warehouse, request.data.get('num'), True)
        else:
            request.data['sendtime'] = None
            statusChangedChuku(self.get_object(), warehouse, request.data.get('num'))

        return super(AdminChukuViewSet, self).update(request, args, kwargs)
