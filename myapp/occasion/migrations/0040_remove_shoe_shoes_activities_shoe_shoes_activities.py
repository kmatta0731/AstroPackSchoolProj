# Generated by Django 4.1.5 on 2023-03-04 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0039_remove_shoe_shoes_activities_shoe_shoes_activities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='shoes_activities',
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_activities',
            field=models.CharField(default='', max_length=150),
        ),
    ]
