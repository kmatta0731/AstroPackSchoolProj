# Generated by Django 4.1.5 on 2023-03-01 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0017_remove_accessorie_accessories_temp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Weather',
        ),
        migrations.RemoveField(
            model_name='electronic',
            name='electronic_gender',
        ),
        migrations.RemoveField(
            model_name='occasion',
            name='occasion_gender',
        ),
    ]
