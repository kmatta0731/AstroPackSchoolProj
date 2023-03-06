# Generated by Django 4.1.5 on 2023-03-06 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0050_remove_generated_list_gen_clothing_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_accessories',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_comfort',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_electronic',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_essentials',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_health',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_shoe',
        ),
        migrations.RemoveField(
            model_name='generated_list',
            name='gen_toiletries',
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_accessories',
            field=models.ManyToManyField(to='occasion.accessorie'),
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_comfort',
            field=models.ManyToManyField(to='occasion.comfort'),
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_electronic',
            field=models.ManyToManyField(to='occasion.electronic'),
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_essentials',
            field=models.ManyToManyField(to='occasion.essential'),
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_health',
            field=models.ManyToManyField(to='occasion.health'),
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_shoe',
            field=models.ManyToManyField(to='occasion.shoe'),
        ),
        migrations.AddField(
            model_name='generated_list',
            name='gen_toiletries',
            field=models.ManyToManyField(to='occasion.toiletrie'),
        ),
    ]