# Generated by Django 4.1.5 on 2023-03-06 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0051_remove_generated_list_gen_accessories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='shoes_occasion',
        ),
        migrations.RemoveField(
            model_name='shoe',
            name='shoes_temperature',
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_occasion',
            field=models.ManyToManyField(to='occasion.occasion'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_temperature',
            field=models.ManyToManyField(to='occasion.temprange'),
        ),
    ]
