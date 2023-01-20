from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from tasks.models import Board

from tasks.serializers import BoardSerializer
from rest_framework import permissions


from rest_framework import viewsets

# Create your views here.

class BoardDetailView(APIView):
    ''''''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my_workspace.html'

    def get(self, request):
        # board = get_object_or_404(Board, owner=request.user)
        board = Board.objects.filter(owner=request.user)
        serializer = BoardSerializer(board)
        return Response({'serializer': serializer, 'all_boards': board})

    def post(self, request):
        print('POST запустился---------------')
        # board = get_object_or_404(Board, owner=request.user)
        board = Board.objects.filter(owner=self.request.user)
        # board = Board.objects.get(owner=self.request.user)
        # serializer = BoardSerializer(board, data=request.data)
        serializer = BoardSerializer(data=request.data)

        if not serializer.is_valid():
            print('не валидна ------------------')
            # return Response({'serializer': serializer, 'boards': board})
            return Response(serializer)
        print('пытаемся сохранить ------------------')
        # serializer.owner
        serializer.save
        print('сохранили ------------------')
        print(serializer)
        return redirect('/')



# class BoardDetailView(viewsets.ModelViewSet):
#     queryset = Board.objects.all()
#     serializer_class = BoardSerializer
#     permission_classes = [permissions.IsAuthenticated]
