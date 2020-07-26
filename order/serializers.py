import json

from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    content = serializers.JSONField()
    fee  = serializers.FloatField(required=False, allow_null=True)
    type = serializers.CharField(required=False, allow_null=True)
    status = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance: Order):
        instance.content = json.loads(instance.content)
        return super(OrderSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['content'] = json.dumps(data['content'])
        return super(OrderSerializer, self).to_internal_value(data)

