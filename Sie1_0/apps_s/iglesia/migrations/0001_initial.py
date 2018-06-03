# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-03 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoPequenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True)),
                ('numero_de_miembos', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Grupo peque\xf1o',
                'verbose_name_plural': 'Grupos peque\xf1os',
            },
        ),
        migrations.CreateModel(
            name='Iglesia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Iglesia',
                'verbose_name_plural': 'Iglesias',
            },
        ),
        migrations.AddField(
            model_name='grupopequenio',
            name='iglesia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iglesia.Iglesia'),
        ),
    ]
