# Generated by Django 4.0.4 on 2022-06-21 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineApp', '0005_alter_users_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='User_Role',
            new_name='UserRole',
        ),
    ]
