# Generated by Django 5.0.6 on 2024-07-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sidequest', '0010_alter_character_class_name_alter_character_race'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('health', models.IntegerField(default=100)),
            ],
        ),
    ]
