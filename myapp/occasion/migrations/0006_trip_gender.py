# Generated by Django 4.1.5 on 2023-02-19 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0005_trip_trip_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='gender',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]