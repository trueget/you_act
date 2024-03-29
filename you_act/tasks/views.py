from django.shortcuts import render, redirect

# from django.views.generic.detail import DetailView
from django.views import View

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer, HTMLFormRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view

from tasks.models import Board, Column, Tasks
from tasks.serializers import BoardSerializer, ColumnSerializer, TaskSerializer

from django.urls import reverse

from django.http.response import JsonResponse
from rest_framework import status

from tasks.forms import TasksForm, ColumnForm


# Create your views here.

class BoardDetailView(APIView):
    '''мои доски и форма создания доски'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/my_boards.html'

    def get(self, request):
        board = Board.objects.filter(owner=request.user)
        serializer = BoardSerializer(board)
        return Response({'serializer': serializer, 'all_boards': board, 'column_id': -1})

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return redirect('tasks:my-boards')
        return Response(serializer)


# class ColumnDetailView(APIView):
#     '''колонки доски и форма создания колонки'''
#     renderer_classes = [TemplateHTMLRenderer, HTMLFormRenderer]
#     template_name = 'tasks/my_columns.html'

#     def get(self, request, pk):
#         board = Board.objects.get(pk=pk)
#         columns = Column.objects.filter(board=board)
#         serializer = ColumnSerializer(columns)

#         all_tasks_on_board = []
#         for column in columns:
#             tasks_in_column = Tasks.objects.filter(column=column)
#             all_tasks_on_board.append(tasks_in_column)

#         return Response({'serializer': serializer, 'columns': columns, 'board': board, 'all_tasks_on_board': all_tasks_on_board})

#     def post(self, request, pk):
#         board = Board.objects.get(pk=pk)
#         serializer = ColumnSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(board=board)
#             return redirect(reverse('tasks:my-board', args=[pk]))
#         return Response(serializer)


# class TaskDetailView(APIView):
#     '''колонка тасок и форма создания тасок'''
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tasks/my_tasks.html'

#     def get(self, request, pk):
#         column = Column.objects.get(pk=pk)
#         tasks_in_column = Tasks.objects.filter(column=column)
#         serializer = TaskSerializer(tasks_in_column)
#         return Response({'serializer': serializer, 'tasks_in_column': tasks_in_column, 'column': column})

#     def post(self, request, pk):
#         column = Column.objects.get(pk=pk)
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(column=column)
#             return redirect(reverse('tasks:my-column', args=[pk]))
#         return Response(serializer)


# @api_view(['PUT', 'DELETE'])
def delete_board(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('tasks:my-boards')


def delete_column(request, pk):
    column = Column.objects.get(pk=pk)
    column.delete()
    return redirect(reverse('tasks:my-board', args=[column.board.id]))


def delete_task(request, pk):
    task = Tasks.objects.get(pk=pk)
    task.delete()
    return redirect(reverse('tasks:my-board', args=[task.column.board.id]))


def create_task(request, pk):
    '''обрабатываем форму для создания задачи с ColumnAndTaskManagement'''
    if request.method == 'POST':
        if 'task-form' in request.POST:
            form = TasksForm(request.POST)
            column = Column.objects.get(pk=pk)
            if form.is_valid():
                tittle = form.cleaned_data['tittle']
                description = form.cleaned_data['description']
                new_task = Tasks(tittle=tittle, column=column, description=description)
                new_task.save()
                return redirect(reverse('tasks:my-board', args=[column.board.pk]))


class ColumnAndTaskManagement(View):
    '''формы колонок и тасок и вывод их значений'''
    template_name = 'tasks/my_columns.html'
    column_form = ColumnForm
    task_form = TasksForm
    click = False

    def get(self, request, pk):
        form1 = self.column_form(None)
        form2 = self.task_form(None)
        board = Board.objects.get(pk=pk)
        columns = Column.objects.filter(board=board)
        data = []
        for column in columns:
            tasks_in_column = Tasks.objects.filter(column=column)

            data.append({'column': column, 'tasks_in_column': tasks_in_column})

        context = {
            'click': self.click,

            'data': data,
            'column_form': form1,
            'task_form': form2,
            'board': board,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        if request.method == 'POST':
            if 'column-form' in request.POST:
                board = Board.objects.get(pk=pk)
                form = ColumnForm(self.request.POST)
                if form.is_valid():
                    name_column = form.cleaned_data['name_column']
                    new_column = Column(name_column=name_column, board=board)
                    new_column.save()
                    return redirect(reverse('tasks:my-board', args=[pk]))

        return render(request, self.template_name, {'column-form': self.column_form, 'task-form': self.task_form})
