# Generated by Django 4.1.5 on 2023-03-06 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0048_remove_clothing_clothing_activity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_gender',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_weather',
        ),
    ]
