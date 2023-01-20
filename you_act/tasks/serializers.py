from rest_framework import serializers
from tasks.models import Board


class BoardSerializer(serializers.ModelSerializer):
    name_board = serializers.CharField(max_length=100, default='My project')

    class Meta:
        model = Board
        fields = '__all__'
        # fields = ('name_board', 'owner')
