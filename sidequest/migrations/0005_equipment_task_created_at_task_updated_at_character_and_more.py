# Generated by Django 5.0.6 on 2024-07-03 15:10

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidequest', '0004_task_repetitive'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('attack', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_stats_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('character_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidequest.character')),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sidequest.equipment')),
            ],
        ),
    ]
