# Generated by Django 4.1.5 on 2023-02-19 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0006_trip_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='num_days',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
