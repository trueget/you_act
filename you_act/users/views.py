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
from users.forms import UpdateUserProfileForm

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

def index(request):
    return render(request, 'index.html', {'user': request.user})






# @method_decorator(login_required, name='dispatch')
class UserProfileView(View):
    '''страница пользователя'''
    model = UserProfile
    template_name = 'user-profile.html'

    def get(self, request, *args, **kwargs):
        user_detail = self.model.objects.filter(user = request.user)
        context = {'user_profile' : user_detail}
        return render(request, self.template_name, context = context)


# @method_decorator(login_required, name='dispatch')
class UpdateUserProfileView(UpdateView):
    '''обновление страницы пользователя'''
    model = UserProfile
    form_class = UpdateUserProfileForm
    template_name = 'user-profile-update.html'

    def get_object(self):
        obj = self.model.objects.get(pk = self.request.user.pk)
        return obj

    def get_success_url(self):
        return reverse('my-profile')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                user_profile = self.model.objects.get(user=request.user)
        print('-'*50, form.cleaned_data['vk'], form.cleaned_data['ok'])

        return redirect('update-profile')






class UserRegisterViews(generics.CreateAPIView):
    '''регистрация пользователя'''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )


class UserList(generics.ListAPIView):
    '''все зарегистрированные пользователи'''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    '''информация об одном user'''
    queryset = User.objects.all()
    serializer_class = UserSerializer






class UserProfileAPIView(APIView):
    '''полный список всех userprofiles'''
    def get(self, request):
         userprofile = UserProfile.objects.all()
         serializer = UserProfileSerializer(userprofile, many=True)
         return Response(serializer.data)


class UserProfileDetail(APIView):
    '''обновление профиля позьзователя'''
    def get_object(self, id):
        try:
            return UserProfile.objects.get(id=id)
        except UserProfile.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        userprofile = self.get_object(id)
        serializer = UserProfileSerializer(userprofile)
        return Response(serializer.data)

    def put(self, request, id):
        userprofile = self.get_object(id)
        serializer = UserProfileSerializer(userprofile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, id):
    #     userprofile = self.get_ob(id=id)
    #     userprofile.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
