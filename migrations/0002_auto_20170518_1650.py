# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orgweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrgModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
            ],
        ),
        migrations.AddField(
            model_name='header',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgweb.OrgModel'),
        ),
    ]
