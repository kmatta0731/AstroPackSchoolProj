# Generated by Django 4.1.5 on 2023-02-17 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0009_gender_gen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='description',
            new_name='shoes_description',
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_gender',
            field=models.ForeignKey(default='Male', on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='gen',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
    ]
