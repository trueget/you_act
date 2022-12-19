from django.shortcuts import render
from django.contrib.auth.models import User

# from rest_framework.views import APIView
# from rest_framework.renderers import TemplateHTMLRenderer
from users.serializers import UserSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.

def index(request):
    return render(request, 'index.html', {'user': request.user})

# class UserPage():



class UserRegisterViews(generics.CreateAPIView):
    '''регистрации пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserList(generics.ListAPIView):
    '''все зарегистрированные пользователи'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''информация об одном пользователе'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
