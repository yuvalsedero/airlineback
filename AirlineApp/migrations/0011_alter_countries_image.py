# Generated by Django 4.0.4 on 2022-08-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AirlineApp', '0010_alter_countries_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='image',
            field=models.ImageField(default='static/images/tamplates/image.jpg', upload_to='images/'),
        ),
    ]