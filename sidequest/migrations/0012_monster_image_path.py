# Generated by Django 5.0.6 on 2024-07-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidequest', '0011_monster'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='image_path',
            field=models.CharField(default='', max_length=100),
        ),
    ]
