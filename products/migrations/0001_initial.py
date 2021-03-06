# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-04 21:40
from __future__ import unicode_literals

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('category', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
    ]