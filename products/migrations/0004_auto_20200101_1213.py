# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-01 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200101_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(choices=[(100, 'A4 (21 x 29.7cm)'), (150, 'A3 (29 x 42cm)'), (200, 'A3 + (32.9 x 48.3cm)')], default=''),
        ),
    ]
