# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-05 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iglesia', '0002_auto_20180605_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iglesia',
            name='direccion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='iglesia',
            name='imagen',
            field=models.ImageField(upload_to=b'imagenes_iglesia'),
        ),
    ]
