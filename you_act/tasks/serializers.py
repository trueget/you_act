from rest_framework import serializers
from tasks.models import Board
from users.serializers import UserSerializer
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User


class BoardSerializer(serializers.ModelSerializer):
    # owner = serializers.SlugRelatedField(write_only=True, slug_field='pk', queryset=User.objects)
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    name_board = serializers.CharField(max_length=100, default='My project')

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    class Meta:
        model = Board
        fields = '__all__'
