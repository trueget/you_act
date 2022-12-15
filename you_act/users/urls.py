from django.urls import path, include
from users.views import index, UserRegisterViews
# from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', index, name='index'),
    # path('register/', UserRegisterViews.as_view, name='register'),
    path('register/', UserRegisterViews.as_view())
]
