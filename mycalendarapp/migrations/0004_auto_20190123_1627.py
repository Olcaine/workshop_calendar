# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-23 15:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendarapp', '0003_auto_20190123_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshopevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Event'),
        ),
    ]
