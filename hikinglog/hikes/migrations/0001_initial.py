# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('date', models.DateField(null=True)),
                ('gain', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('duration', models.DurationField(null=True)),
                ('distance', models.FloatField(null=True)),
                ('region', models.CharField(blank=True, max_length=255)),
                ('park', models.CharField(blank=True, max_length=255)),
                ('weather', models.CharField(blank=True, max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
            ],
        ),
    ]
