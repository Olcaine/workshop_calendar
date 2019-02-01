# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-01 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendarapp', '0005_auto_20190201_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='workshopevent',
            name='equipment',
            field=models.ManyToManyField(to='mycalendarapp.Equipment'),
        ),
        migrations.AlterField(
            model_name='workshopevent',
            name='room',
            field=models.ManyToManyField(to='mycalendarapp.Room'),
        ),
    ]
