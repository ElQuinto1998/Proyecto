# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-04 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0005_auto_20180603_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Peticion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=120, null=True)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario')),
            ],
            options={
                'verbose_name': 'Peticion',
                'verbose_name_plural': 'Peticiones',
            },
        ),
        migrations.AddField(
            model_name='comentario',
            name='petici',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='peticion.Peticion'),
        ),
    ]
