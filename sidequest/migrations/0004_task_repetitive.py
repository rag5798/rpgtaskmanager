# Generated by Django 5.0.6 on 2024-06-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidequest', '0003_alter_task_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='repetitive',
            field=models.BooleanField(default=False),
        ),
    ]
