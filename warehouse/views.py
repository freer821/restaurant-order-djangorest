import json

import django_filters

# Create your views here.
from django.utils import timezone
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
    serializer_class = AdminWarehouseSerializer
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
