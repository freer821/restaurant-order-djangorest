import json

from rest_framework import serializers

from ruku.models import Forecast


class UserForecastSerializer(serializers.ModelSerializer):
    arrivedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    extra = serializers.JSONField()

    class Meta:
        model = Forecast
        exclude = ['owner', 'updatedtime']
        extra_kwargs = {
            'arrivedtime': {'read_only': True},
            'real_num': {'read_only': True},
            'admin_extra': {'read_only': True}
        }

    def to_representation(self, instance: Forecast ):
        instance.extra = json.loads(instance.extra)
        return super(UserForecastSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['extra'] = json.dumps(data['extra'])
        return super(UserForecastSerializer, self).to_internal_value(data)