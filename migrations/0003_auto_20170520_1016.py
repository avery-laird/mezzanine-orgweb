# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-20 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgweb', '0002_auto_20170518_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgmodel',
            name='description',
            field=models.TextField(blank=True, max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='orgmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orgweb.Profile'),
            preserve_default=False,
        ),
    ]
