# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 16:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chronicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=50)),
                ('q2', models.TextField()),
                ('q3', models.TextField()),
                ('name', models.CharField(default='', max_length=50)),
                ('is_correct1', models.BooleanField(default=False)),
                ('is_correct2', models.BooleanField(default=False)),
                ('is_correct3', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)])),
                ('reviewer_1', models.TextField(default='')),
                ('reviewer_2', models.TextField(default='')),
                ('reviewer_3', models.TextField(default='')),
                ('day_to_slot', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('is_selected', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.Info')),
            ],
        ),
    ]
