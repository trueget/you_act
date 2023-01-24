from rest_framework import serializers
from tasks.models import Board, Column


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    name_board = serializers.CharField(max_length=100, default='My project')

    class Meta:
        model = Board
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = '__all__'
