# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-21 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendarapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshopevent',
            name='gear',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='workshopevent',
            name='room',
            field=models.CharField(default='none', max_length=120),
        ),
    ]
