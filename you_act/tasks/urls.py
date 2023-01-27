from django.urls import path, include
from tasks.views import (
    BoardDetailView,
    ColumnDetailView,
    TaskDetailView,
    # DeleteColumn,
    delete_column,
)

from rest_framework import routers


app_name = 'tasks'


urlpatterns = [
    path('my-boards/', BoardDetailView.as_view(), name='my-boards'),
    path('my-board/<int:pk>/', ColumnDetailView.as_view(), name='my-board'),

    path('my-column/<int:pk>/', TaskDetailView.as_view(), name='my-column'),
    path('delete-column/<int:pk>/', delete_column, name='delete-column'),
    # path('delete-column/<int:pk>/', DeleteColumn.as_view(), name='delete-column'),
]
