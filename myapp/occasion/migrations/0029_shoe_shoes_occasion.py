# Generated by Django 4.1.5 on 2023-03-04 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0028_remove_shoe_shoes_activities_shoe_shoes_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoes_occasion',
            field=models.CharField(default='Leisure', max_length=150),
        ),
    ]
