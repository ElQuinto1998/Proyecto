# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-05 02:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20180603_1835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
    ]
