import json

from rest_framework import serializers

from config import settings
from goods.models import Category, Good, FileManagement


class GoodSerializer(serializers.ModelSerializer):
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    content = serializers.JSONField()
    class Meta:
        model = Good
        fields = '__all__'

    def to_representation(self, instance: Good):
        instance.content = json.loads(instance.content)
        return super(GoodSerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['content'] = json.dumps(data['content'])
        return super(GoodSerializer, self).to_internal_value(data)


class CategorySerializer(serializers.ModelSerializer):
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    content = serializers.JSONField()
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance: Category):
        instance.content = json.loads(instance.content)
        return super(CategorySerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['content'] = json.dumps(data['content'])
        return super(CategorySerializer, self).to_internal_value(data)


class FileManagementSerializer(serializers.ModelSerializer):
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    name = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 文件名称
    size = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 文件大小
    url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        request = self.context.get('request')
        file_url = '%s%s' % (settings.STATIC_URL, obj.file)
        return request.build_absolute_uri(file_url)

    class Meta:
        model = FileManagement
        fields = '__all__'



class UserCategorySerializer(serializers.ModelSerializer):
    content = serializers.JSONField()

    class Meta:
        model = Category
        fields = ['name', 'content']

    def to_representation(self, instance: Category):
        instance.content = json.loads(instance.content)
        return super(UserCategorySerializer, self).to_representation(instance)

    def to_internal_value(self, data):
        data['content'] = json.dumps(data['content'])
        return super(UserCategorySerializer, self).to_internal_value(data)
