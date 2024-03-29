# Generated by Django 4.1.5 on 2023-03-02 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0019_activities'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='activities',
            field=models.ManyToManyField(to='occasion.activities'),
        ),
        migrations.AlterField(
            model_name='accessorie',
            name='accessories_gender',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AlterField(
            model_name='clothing',
            name='clothing_gender',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AlterField(
            model_name='comfort',
            name='comfort_gender',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AlterField(
            model_name='health',
            name='health_gender',
            field=models.ForeignKey(blank=True, default=3, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='shoes_gender',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AlterField(
            model_name='toiletrie',
            name='toiletries_gender',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
    ]
