# Generated by Django 4.1.5 on 2023-03-06 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0053_remove_shoe_shoes_activities_shoe_shoes_activities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipment',
            old_name='clothing_activity',
            new_name='equipment_activity',
        ),
        migrations.RenameField(
            model_name='equipment',
            old_name='clothing_occasion',
            new_name='equipment_occasion',
        ),
    ]
