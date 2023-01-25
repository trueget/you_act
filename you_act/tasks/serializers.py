from rest_framework import serializers
from tasks.models import Board, Column, Tasks


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    name_board = serializers.CharField(max_length=100, default='New project')

    class Meta:
        model = Board
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    name_column = serializers.CharField(max_length=100, default='New column')
    board = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Column
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    column = serializers.PrimaryKeyRelatedField(read_only=True)
    tittle = serializers.CharField(max_length=100, default='New task')

    class Meta:
        model = Tasks
        fields = '__all__'
