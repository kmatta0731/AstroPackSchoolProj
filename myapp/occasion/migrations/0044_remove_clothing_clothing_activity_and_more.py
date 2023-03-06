# Generated by Django 4.1.5 on 2023-03-05 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0043_remove_clothing_clothing_occasion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothing',
            name='clothing_activity',
        ),
        migrations.AddField(
            model_name='clothing',
            name='clothing_activity',
            field=models.ManyToManyField(to='occasion.activities'),
        ),
    ]
