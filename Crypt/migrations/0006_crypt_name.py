# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crypt', '0005_auto_20170718_0403'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypt',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
