from rest_framework import serializers
from users.models import UserProfile
from django.contrib.auth.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
