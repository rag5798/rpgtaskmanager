# myapp/forms.py

from django import forms


from django import forms
from .models import UserData

class UserDataForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'password']  # Specify the fields you want in the form

