from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=30, null=False)
    task_description = models.CharField(max_length=50, null=True)
    completed = models.BooleanField(default=False, null=True)
    task_completion_counter = models.IntegerField(default=0, null=True)
    repetitive = models.BooleanField(default=False)


class CharacterStats:
    pass

