# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-11 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendarapp', '0002_auto_20190207_1100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipment',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('location',)},
        ),
    ]
