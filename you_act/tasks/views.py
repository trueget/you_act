from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from tasks.models import Board, Column, Tasks
from tasks.serializers import BoardSerializer, ColumnSerializer, TaskSerializer
from django.urls import reverse


# Create your views here.

class BoardDetailView(APIView):
    '''мои доски и форма создания доски'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/my_boards.html'

    def get(self, request):
        board = Board.objects.filter(owner=request.user)
        serializer = BoardSerializer(board)
        return Response({'serializer': serializer, 'all_boards': board})

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return redirect('tasks:my-boards')
        return Response(serializer)


class ColumnDetailView(APIView):
    '''колонки доски и форма создания колонки'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/my_columns.html'

    def get(self, request, pk):
        board = Board.objects.get(pk=pk)
        columns = Column.objects.filter(board=board)
        serializer = ColumnSerializer(columns)
        return Response({'serializer': serializer, 'columns': columns, 'board': board})

    def post(self, request, pk):
        board = Board.objects.get(pk=pk)
        serializer = ColumnSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=board)
            return redirect(reverse('tasks:my-board', args=[pk]))
        return Response(serializer)


class TaskDetailView(APIView):
    ''''''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/my_tasks.html'

    def get(self, request, pk):
        column = Column.objects.get(pk=pk)
        tasks_in_column = Tasks.objects.filter(column=column)
        serializer = TaskSerializer(tasks_in_column)
        return Response({'serializer': serializer, 'tasks_in_column': tasks_in_column, 'column': column})

    def post(self, request, pk):
        column = Column.objects.get(pk=pk)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(column=column)
            return redirect(reverse('tasks:my-column', args=[pk]))
        return Response(serializer)
