# Generated by Django 4.0.4 on 2023-07-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcities',
            name='country_short',
            field=models.CharField(default='', max_length=10),
        ),
    ]
