# Generated by Django 4.1.5 on 2023-03-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0052_remove_shoe_shoes_occasion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='shoes_activities',
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_activities',
            field=models.ManyToManyField(to='occasion.activities'),
        ),
    ]
