# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('btapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('proyecto', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='images/data', blank=True)),
                ('descripcion', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=8)),
                ('empresa', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('imagen', models.ImageField(upload_to='images/data', blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='destacado',
            field=models.BooleanField(default='false'),
        ),
    ]
