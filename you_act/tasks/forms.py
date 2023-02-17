from django.forms import ModelForm, Textarea, TextInput
from tasks.models import Tasks, Column


class ColumnForm(ModelForm):

    class Meta:
        model = Column
        fields = ['name_column']

        widgets = {
            'name_column': TextInput(attrs={
                'placeholder': 'Enter column name...',
            })
        }


class TasksForm(ModelForm):

    class Meta:
        model = Tasks
        fields = ['tittle', 'description']

        widgets = {
            'tittle': TextInput(attrs={
                'placeholder': 'Enter task name...',
            }),
            'description': Textarea(attrs={
                'placeholder': 'Describe the task...',
                'rows': 4
            })
        }
