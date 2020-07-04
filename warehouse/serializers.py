import json

from rest_framework import serializers

from warehouse.models import *


class WarehouseSerializer(serializers.ModelSerializer):
    arrivedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)

    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseDetailSerializer(serializers.ModelSerializer):
    arrivedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    descrp = serializers.JSONField(required=True)
    sn_code = serializers.CharField(required=True)
    product_name = serializers.CharField(required=True)
    status = serializers.CharField(required=True)

    class Meta:
        model = WarehouseDetail
        fields = '__all__'

    def to_representation(self, instance: WarehouseDetail):
        instance.descrp = json.loads(instance.descrp)
        return super(WarehouseDetailSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['descrp'] = json.dumps(data['descrp'])
        return super(WarehouseDetailSerializer, self).to_internal_value(data)
