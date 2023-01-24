from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tasks.models import Board, Column
from tasks.serializers import BoardSerializer, ColumnSerializer

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
            return redirect('/')
        return Response(serializer)

# class BoardDetailView(viewsets.ModelViewSet):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     permission_classes = [permissions.IsAuthenticated]



class ColumnDetailView(APIView):
    '''колонки доски и форма создания колонки'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tasks/my_columns.html'

    def get(self, request, pk):
        board = Board.objects.get(pk=pk)
        column = Column.objects.filter(board=board)
        serializer = ColumnSerializer(column)
        return Response({'serializer': serializer, 'columns': column})
