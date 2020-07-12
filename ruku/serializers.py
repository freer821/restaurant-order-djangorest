import json

from rest_framework import serializers

from ruku.models import Forecast


class UserForecastSerializer(serializers.ModelSerializer):
    arrivedtime = serializers.DateTimeField(format="%Y-%m-%d", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d", allow_null=True, required=False)
    logistic_company = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    extra = serializers.JSONField()

    class Meta:
        model = Forecast
        exclude = ['owner', 'updatedtime']
        extra_kwargs = {
            'arrivedtime': {'read_only': True},
            'real_num': {'read_only': True},
            'admin_extra': {'read_only': True}
        }

    def to_representation(self, instance: Forecast):
        if instance.extra:
            instance.extra = json.loads(instance.extra)
        return super(UserForecastSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        if 'extra' in data:
            data['extra'] = json.dumps(data['extra'])
        return super(UserForecastSerializer, self).to_internal_value(data)


class AdminForecastSerializer(serializers.ModelSerializer):
    arrivedtime = serializers.DateTimeField(format="%Y-%m-%d", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    extra = serializers.JSONField(required=False)
    admin_extra = serializers.JSONField(required=False)

    class Meta:
        model = Forecast
        fields = '__all__'

    def to_representation(self, instance: Forecast):
        if instance.extra:
            instance.extra = json.loads(instance.extra)
        if instance.admin_extra:
            instance.admin_extra = json.loads(instance.admin_extra)
        return super(AdminForecastSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        if 'extra' in data:
            data['extra'] = json.dumps(data['extra'])
        if 'admin_extra' in data:
            data['admin_extra'] = json.dumps(data['admin_extra'])
        return super(AdminForecastSerializer, self).to_internal_value(data)
