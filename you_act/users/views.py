from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView
from django.views import View
from django.http import HttpResponse

# from rest_framework.views import APIView
# from rest_framework.renderers import TemplateHTMLRenderer
from users.serializers import UserSerializer, UserProfileSerializer
from users.models import UserProfile

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return render(request, 'index.html', {'user': request.user})


class UserRegisterViews(generics.CreateAPIView):
    '''регистрация пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class MyProfileDetail(APIView):
    '''обновление страницы пользователя и вывод данных в свой шаблон'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'my_profile.html'

    def get(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = UserProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request):
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = UserProfileSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        return redirect('/')


class ProfileList(APIView):
    '''список пользователей'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request):
        queryset = UserProfile.objects.all()
        return Response({'profiles': queryset})


class ProfileDetail(APIView):
    '''информация о пользователе'''
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_profile.html'

    def get(self, request, pk):
        profile = get_object_or_404(UserProfile, pk=pk)
        serializer = UserProfileSerializer(profile)
        return Response({'serializer': serializer, 'profile': profile})
