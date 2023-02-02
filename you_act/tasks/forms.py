from django.forms import ModelForm
from tasks.models import Tasks, Column


class ColumnForm(ModelForm):

    class Meta:
        model = Column
        fields = ['name_column']


class TasksForm(ModelForm):

    class Meta:
        model = Tasks
        fields = ['tittle']
