import json

from rest_framework import serializers

from chuku.models import Chuku


class UserChukuSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(required=True)
    sn_code = serializers.CharField(required=False)
    type = serializers.CharField(required=True) # 物品类型
    platform = serializers.CharField(required=False)  # 平台
    contact = serializers.CharField(required=False)  # 负责人
    pack_type = serializers.CharField(required=False)  # 纸箱
    pack_content = serializers.CharField(required=False)  # 内物类型
    logistic_type = serializers.CharField(required=False)  # 物流类型
    num = serializers.BooleanField(required=False)
    sendtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    reciever = serializers.JSONField(required=False)

    class Meta:
        model = Chuku
        exclude = ['owner', 'updatedtime']
        extra_kwargs = {
            'sendtime': {'read_only': True},
            'comment': {'read_only': True},
            'logistic_code': {'read_only': True},
            'logistic_company': {'read_only': True},
            'weight': {'read_only': True},
            'long': {'read_only': True},
            'width': {'read_only': True},
            'heigh': {'read_only': True},
            'fba_code': {'read_only': True},
            'arrivedtime': {'read_only': True},
            'status': {'read_only': True}
        }

    def to_representation(self, instance: Chuku):
        instance.reciever = json.loads(instance.reciever)
        return super(UserChukuSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['reciever'] = json.dumps(data['reciever'])
        return super(UserChukuSerializer, self).to_internal_value(data)
