# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marque', models.CharField(max_length=64)),
                ('annee', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('description', models.TextField(blank=True)),
                ('cylindree', models.CharField(max_length=32, blank=True)),
                ('proprietaire', models.CharField(max_length=64)),
                ('photo', models.ImageField(upload_to=b'photos/%Y-%m', blank=True)),
            ],
            options={
                'ordering': ('marque', 'annee', 'proprietaire'),
                'verbose_name': 'Voiture',
                'verbose_name_plural': 'Voitures',
            },
        ),
    ]
