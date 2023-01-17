from django.urls import path
from users.views import (
    index, 
    UserRegisterViews, 
    MyProfileDetail,
    ProfileList,
    ProfileDetail,
    )
from django.contrib.auth import views as auth_views


app_name = 'users'


urlpatterns = [
    path('', index, name='index'),
    path('register/', UserRegisterViews.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),

    path('profile-list/', ProfileList.as_view(), name='profile-list'),
    path('user-profile/<int:pk>/', ProfileDetail.as_view(), name='user-profile'),

    path('my-profile/', MyProfileDetail.as_view(), name='my-profile'),
]
