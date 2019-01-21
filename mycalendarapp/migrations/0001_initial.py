# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-21 09:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0011_event_calendar_not_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Event')),
            ],
        ),
    ]
