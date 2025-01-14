# Generated by Django 5.0.1 on 2024-10-15 08:17

import django.db.models.deletion
import location_field.models.plain
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellHouses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('second_image', models.ImageField(upload_to='second_uploads/')),
                ('third_image', models.ImageField(upload_to='uploads/')),
                ('fourth_image', models.ImageField(upload_to='uploads/')),
                ('details', models.CharField(max_length=100)),
                ('bedroom', models.IntegerField()),
                ('bathroom', models.IntegerField()),
                ('area_square', models.IntegerField()),
                ('garage', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('built_year', models.DateField()),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('posted_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('sellhouses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='house_sales.sellhouses')),
            ],
            bases=('house_sales.sellhouses',),
        ),
        migrations.CreateModel(
            name='Buildings',
            fields=[
                ('sellhouses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='house_sales.sellhouses')),
            ],
            bases=('house_sales.sellhouses',),
        ),
        migrations.CreateModel(
            name='Condominum',
            fields=[
                ('sellhouses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='house_sales.sellhouses')),
            ],
            bases=('house_sales.sellhouses',),
        ),
        migrations.CreateModel(
            name='GroundPlus',
            fields=[
                ('sellhouses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='house_sales.sellhouses')),
            ],
            bases=('house_sales.sellhouses',),
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('sellhouses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='house_sales.sellhouses')),
            ],
            bases=('house_sales.sellhouses',),
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('sellhouses_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='house_sales.sellhouses')),
            ],
            bases=('house_sales.sellhouses',),
        ),
    ]
