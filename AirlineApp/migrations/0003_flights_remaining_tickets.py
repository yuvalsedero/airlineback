# Generated by Django 4.0.4 on 2022-06-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineApp', '0002_alter_users_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='Remaining_Tickets',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]