# Generated by Django 4.0.3 on 2024-06-21 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_profile_user_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_room',
        ),
    ]
