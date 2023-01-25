from django.urls import path, include
from tasks.views import BoardDetailView, ColumnDetailView, TaskDetailView

from rest_framework import routers


app_name = 'tasks'


# router = routers.DefaultRouter()
# router.register(r'my_workspace', BoardDetailView)


urlpatterns = [
    # path('', include(router.urls)),
    path('my-boards/', BoardDetailView.as_view(), name='my-boards'),
    path('my-board/<int:pk>/', ColumnDetailView.as_view(), name='my-board'),
    path('my-column/<int:pk>', TaskDetailView.as_view(), name='my-column'),
]
