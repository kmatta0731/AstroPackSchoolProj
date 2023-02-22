# Generated by Django 4.1.5 on 2023-02-22 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('occasion', '0008_rename_num_days_trip_length_of_trip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Generated_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_qty_of_clothing', models.CharField(max_length=150)),
                ('gen_weather', models.CharField(max_length=150)),
                ('gen_description', models.CharField(default='Test Desc', max_length=150)),
                ('gen_accessories', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.accessorie')),
                ('gen_clothing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.clothing')),
                ('gen_comfort', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.comfort')),
                ('gen_electronic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.electronic')),
                ('gen_essentials', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.essential')),
                ('gen_gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender')),
                ('gen_health', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.health')),
                ('gen_item_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category')),
                ('gen_occasion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.occasion')),
                ('gen_shoe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.shoe')),
                ('gen_toiletries', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.toiletrie')),
                ('gen_tripID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.trip')),
            ],
        ),
        migrations.AddField(
            model_name='accessorie',
            name='accessories_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='accessorie',
            name='accessories_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='clothing_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='clothing',
            name='clothing_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='comfort',
            name='comfort_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='comfort',
            name='comfort_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='electronic',
            name='electronic_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='electronic',
            name='electronic_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='essential',
            name='essentials_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='essential',
            name='essentials_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='health',
            name='health_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='health',
            name='health_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='occasion',
            name='occasion_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='occasion',
            name='occasion_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='shoe',
            name='shoes_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
        migrations.AddField(
            model_name='toiletrie',
            name='toiletries_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.gender'),
        ),
        migrations.AddField(
            model_name='toiletrie',
            name='toiletries_item_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='occasion.item_category'),
        ),
    ]
