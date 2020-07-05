import json

from rest_framework import serializers

from chuku.models import Chuku


class UserChukuSerializer(serializers.ModelSerializer):
    sn_code = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    type = serializers.CharField(allow_blank=True, allow_null=True, required=False) # 物品类型
    platform = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 平台
    contact = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 负责人
    pack_type = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 纸箱
    pack_content = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 内物类型
    logistic_type = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 物流类型
    logistic_code = serializers.CharField(allow_blank=True, allow_null=True, required=False)  #
    fba_code = serializers.CharField(allow_blank=True, allow_null=True, required=False)  #
    logistic_company = serializers.CharField(allow_blank=True, allow_null=True, required=False)  #

    weight = serializers.FloatField(allow_null=True, required=False)
    sendtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    reciever = serializers.JSONField(allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)

    class Meta:
        model = Chuku
        exclude = ['owner', 'updatedtime']
        extra_kwargs = {
            'sendtime': {'read_only': True},
            'comment': {'read_only': True},
            'status': {'read_only': True}
        }

    def to_representation(self, instance: Chuku):
        instance.reciever = json.loads(instance.reciever)
        return super(UserChukuSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['reciever'] = json.dumps(data['reciever'])
        return super(UserChukuSerializer, self).to_internal_value(data)


class AdminChukuSerializer(serializers.ModelSerializer):
    sn_code = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    type = serializers.CharField(allow_blank=True, allow_null=True, required=False) # 物品类型
    platform = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 平台
    contact = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 负责人
    pack_type = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 纸箱
    pack_content = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 内物类型
    logistic_type = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 物流类型
    logistic_code = serializers.CharField(allow_blank=True, allow_null=True, required=False)  #
    fba_code = serializers.CharField(allow_blank=True, allow_null=True, required=False)  #
    logistic_company = serializers.CharField(allow_blank=True, allow_null=True, required=False)  #

    weight = serializers.FloatField(allow_null=True, required=False)
    sendtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    reciever = serializers.JSONField(allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)

    class Meta:
        model = Chuku
        fields = '__all__'

    def to_representation(self, instance: Chuku):
        instance.reciever = json.loads(instance.reciever)
        return super(UserChukuSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['reciever'] = json.dumps(data['reciever'])
        return super(UserChukuSerializer, self).to_internal_value(data)
