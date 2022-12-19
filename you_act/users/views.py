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


# class UserRegisterViews(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'registration/register.html'

#     def get(self, request, pk):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(user)
#         return Response({'serializer': serializer, 'user': user})

#     def post(self, request, pk):
#         user = get_object_or_404(User, pk=pk)
#         serializer = UserSerializer(user, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'user': user})
#         serializer.save()
#         return redirect('index')

class UserRegisterViews(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
