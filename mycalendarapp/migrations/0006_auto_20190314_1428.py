# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-14 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendarapp', '0005_animator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animator',
            name='user',
        ),
        migrations.DeleteModel(
            name='Animator',
        ),
    ]
