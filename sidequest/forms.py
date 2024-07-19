# myapp/forms.py

from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import UserData, Task, Character
import random

class UserDataForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']  # Specify the fields you want in the form

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user_id','task_name','task_description','completed','task_completion_counter']

class TaskCreationForm(forms.ModelForm):
    repetitive = forms.BooleanField(required=False, label='Repetitive Task')

    class Meta:
        model = Task
        fields = ['task_name', 'task_description']

class CharacterCreationForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['character_name']  # Only include character_name in the form

    def save(self, user, commit=True):
        # Create the character instance with the provided character_name
        character = super().save(commit=False)
        character.user = user  # Set the user for the character
        character.class_name = 'barbarian'  # Default value for class_name
        character.race = 'human'  # Default value for race
        character.level = 0  # Default level
        character.attacks = 0  # Default attacks

        # Assign random stats between 1 and 20
        character.strength = random.randint(1, 20)
        character.dexterity = random.randint(1, 20)
        character.constitution = random.randint(1, 20)
        character.intelligence = random.randint(1, 20)
        character.wisdom = random.randint(1, 20)
        character.charisma = random.randint(1, 20)

        if commit:
            character.save()
        return character


