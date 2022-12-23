from django.urls import path
from users.views import (
    index, 
    UserProfileView,
    UpdateUserProfileView,

    UserRegisterViews, 
    UserList, 
    UserDetail, 
    # UserProfileList
    UserProfileAPIView,
    UserProfileDetail,
    )
from django.contrib.auth import views as auth_views
# from rest_framework import routers


app_name = 'users'

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', index, name='index'),
    path('register/', UserRegisterViews.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    # path('my_page/', UserProfileList.as_view()),
    path('my_page/', UserProfileAPIView.as_view()),
    path('detail/<int:id>/', UserProfileDetail.as_view()),


    path('my-profile/', UserProfileView.as_view(), name='my-profile'),
    path('update-profile/', UpdateUserProfileView.as_view(), name='update-profile'),
]
