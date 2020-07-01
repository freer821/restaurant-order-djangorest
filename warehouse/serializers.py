import json

from rest_framework import serializers

from warehouse.models import Warehouse


class AdminWarehouseSerializer(serializers.ModelSerializer):
    arrivedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)

    class Meta:
        model = Warehouse
        fields = '__all__'