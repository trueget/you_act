from rest_framework import serializers
from tasks.models import Board
from users.serializers import UserSerializer
from rest_framework.fields import CurrentUserDefault
from django.contrib.auth.models import User


class BoardSerializer(serializers.ModelSerializer):
    # owner = UserSerializer(many=False)
    # owner = UserSerializer(read_only=True, many=False, default=serializers.CurrentUserDefault())
    # owner = UserSerializer(read_only=True, many=False, default=CurrentUserDefault())
    owner = serializers.SlugRelatedField(write_only=True, slug_field='pk', queryset=User.objects)
    name_board = serializers.CharField(max_length=100, default='My project')

    class Meta:
        model = Board
        fields = '__all__'
        # fields = ('id', 'name_board', 'members')

    # def save(self):
    #     owner = CurrentUserDefault()
    #     name_board = self.validated_data['name_board']
    #     members = self.validated_data['members']
