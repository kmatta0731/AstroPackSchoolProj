# Generated by Django 4.1.5 on 2023-03-05 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0041_remove_clothing_clothing_activity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occasion', models.CharField(max_length=150)),
            ],
        ),
    ]