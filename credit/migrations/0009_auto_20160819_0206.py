# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0008_creditrecdata_day_to_slot'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditrecdata',
            name='reviewer_1',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='creditrecdata',
            name='reviewer_2',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='creditrecdata',
            name='reviewer_3',
            field=models.TextField(default=b''),
        ),
    ]
