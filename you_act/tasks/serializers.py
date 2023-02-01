from rest_framework import serializers
from tasks.models import Board, Column, Tasks


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    name_board = serializers.CharField(max_length=100, default='New board')

    class Meta:
        model = Board
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):
    name_column = serializers.CharField(max_length=100, default='New column')
    board = serializers.PrimaryKeyRelatedField(read_only=True)
    # board = BoardSerializer()

    class Meta:
        model = Column
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    tittle = serializers.CharField(max_length=100, default='New task')
    column = serializers.PrimaryKeyRelatedField(read_only=True)
    # column = ColumnSerializer()

    class Meta:
        model = Tasks
        fields = '__all__'
