from abc import ABC

from django.contrib.auth.models import User
from rest_framework import serializers

from config import settings
from config.settings import IS_SEND_REGIST_MAIL
from user.models import Profile, FileManagement
from user.services import sendActiveEmail


class ProfileSerializer(serializers.Serializer):
    company_name = serializers.CharField(allow_blank=False, allow_null=False, required=True)
    company_tel = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    company_addr = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    role = serializers.CharField(allow_blank=True, allow_null=True, required=False)
    status = serializers.CharField(allow_blank=True, allow_null=True, required=False)


class RegisterSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['username']
        )
        user.set_password(validated_data['password'])
        if IS_SEND_REGIST_MAIL:
            user.is_active = False
            sendActiveEmail(validated_data['username'])
        user.save()

        profile_data = validated_data.get('profile', '')
        profile_data['role'] = 'user'

        Profile.objects.create(owner=user, **profile_data)

        return user


class UserRetrieveUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['username', 'is_superuser', 'profile']
        extra_kwargs = {
            'username': {'read_only': True}
        }

    def update(self, instance, validated_data):

        profile_data = validated_data.get('profile', '')
        for key, value in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()

        return instance


class ChangePasswordSerializer(serializers.Serializer):

    """
    Serializer for password change endpoint.
    """
    oldPassword = serializers.CharField(required=True)
    newPassword = serializers.CharField(required=True)


class UserAdminSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)

    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'first_name', 'last_name', 'groups', 'email', 'user_permissions']
        extra_kwargs = {
            'username': {'read_only': True}
        }


class FileManagementSerializer(serializers.ModelSerializer):
    updatedtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    createdtime = serializers.DateTimeField(format="%Y-%m-%d %H:%M", allow_null=True, required=False)
    notes = serializers.CharField(allow_blank=True, allow_null=True, required=False)  # 负责人
    url = serializers.SerializerMethodField('get_file_url')

    def get_file_url(self, obj):
        request = self.context.get('request')
        file_url = '%s%s' % (settings.STATIC_URL, obj.file)
        return request.build_absolute_uri(file_url)


    class Meta:
        model = FileManagement
        exclude = ['owner']
