from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(default=now)

class Character(models.Model):
    character_stats_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100, default='barbarian')
    race = models.CharField(max_length=100, default='human')
    level = models.IntegerField(default=0)
    strength = models.IntegerField(default=10)  # Default value changed to 10
    dexterity = models.IntegerField(default=10)  # Default value changed to 10
    constitution = models.IntegerField(default=10)  # Default value changed to 10
    intelligence = models.IntegerField(default=10)  # Default value changed to 10
    wisdom = models.IntegerField(default=10)  # Default value changed to 10
    charisma = models.IntegerField(default=10)  # Default value changed to 10
    attacks = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    equipment = models.TextField(blank=True, null=True)

class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    attack = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True, editable=False)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)

class Monster(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=100)  # Default health
    image_path = models.CharField(max_length=100, default="")


