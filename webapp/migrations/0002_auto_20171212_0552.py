# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 05:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]