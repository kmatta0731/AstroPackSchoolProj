# Generated by Django 4.1.5 on 2023-03-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0021_alter_shoe_shoes_temperature'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoes_activity',
            field=models.CharField(default='', max_length=150),
        ),
    ]
