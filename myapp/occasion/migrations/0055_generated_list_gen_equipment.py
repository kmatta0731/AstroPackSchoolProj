# Generated by Django 4.1.5 on 2023-03-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0054_rename_clothing_activity_equipment_equipment_activity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='generated_list',
            name='gen_equipment',
            field=models.ManyToManyField(to='occasion.equipment'),
        ),
    ]