# Generated by Django 4.1.5 on 2023-03-04 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0031_alter_clothing_clothing_activity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_occasion',
        ),
        migrations.DeleteModel(
            name='occasion',
        ),
    ]