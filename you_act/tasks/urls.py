from django.urls import path
from tasks.views import (
    BoardDetailView,
    ColumnDetailView,
    TaskDetailView,
    delete_board,
    delete_column,
    delete_task,
    create_task,

)

app_name = 'tasks'


urlpatterns = [
    path('my-boards/', BoardDetailView.as_view(), name='my-boards'),
    path('my-board/<int:pk>/', ColumnDetailView.as_view(), name='my-board'),
    path('delete-board/<int:pk>/', delete_board, name='delete-board'),

    path('my-column/<int:pk>/', TaskDetailView.as_view(), name='my-column'),
    path('delete-column/<int:pk>/', delete_column, name='delete-column'),

    path('delete-task/<int:pk>/', delete_task, name='delete-task'),

    path('create_task_in-column/<int:pk>/', create_task, name='create-task'),

]
