# Generated by Django 4.1.5 on 2023-02-27 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0011_trip_temp_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='shoes_temperature',
            field=models.CharField(choices=[('cold', 'Cold'), ('warm', 'Warm'), ('hot', 'Hot')], default='Warm', max_length=10),
        ),
    ]
