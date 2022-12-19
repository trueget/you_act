from django.urls import path, include
from users.views import index, UserRegisterViews, UserList, UserDetail
from django.contrib.auth import views as auth_views
# from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('', index, name='index'),
    # path('register/', UserRegisterViews.as_view, name='register'),
    path('register/', UserRegisterViews.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login'), name='logout'),

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

]
