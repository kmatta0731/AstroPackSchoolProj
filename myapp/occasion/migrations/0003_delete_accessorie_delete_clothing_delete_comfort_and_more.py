# Generated by Django 4.1.5 on 2023-02-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0002_accessorie_clothing_comfort_electronic_essential_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Accessorie',
        ),
        migrations.DeleteModel(
            name='Clothing',
        ),
        migrations.DeleteModel(
            name='Comfort',
        ),
        migrations.DeleteModel(
            name='Electronic',
        ),
        migrations.DeleteModel(
            name='Health',
        ),
        migrations.DeleteModel(
            name='Shoe',
        ),
        migrations.DeleteModel(
            name='Toiletrie',
        ),
    ]
