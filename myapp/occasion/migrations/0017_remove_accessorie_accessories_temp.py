# Generated by Django 4.1.5 on 2023-02-28 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0016_accessorie_accessories_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessorie',
            name='accessories_temp',
        ),
    ]
