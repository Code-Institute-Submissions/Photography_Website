# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-11-28 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20191127_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email_address', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=30)),
                ('postcode', models.CharField(blank=True, max_length=15)),
                ('town_or_city', models.CharField(max_length=30)),
                ('street_address1', models.CharField(max_length=30)),
                ('street_address2', models.CharField(max_length=30)),
                ('county', models.CharField(blank=True, max_length=30)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
