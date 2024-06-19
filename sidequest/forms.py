# myapp/forms.py

from django import forms


from django import forms
from .models import UserData, Task

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'password']  # Specify the fields you want in the form

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user_id','task_name','task_description','completed','task_completion_counter']


