# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-03 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iglesia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=120, null=True)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField(blank=True, verbose_name='Conversation Date')),
                ('hora', models.TimeField(blank=True, verbose_name='Conversation Time')),
                ('ubicacion', models.CharField(blank=True, max_length=120, null=True)),
                ('imagen', models.ImageField(upload_to=b'imagenes_actividad')),
                ('iglesia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iglesia.Iglesia')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
            },
        ),
    ]
