import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chuku.models import Chuku
from chuku.serializers import UserChukuSerializer
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
