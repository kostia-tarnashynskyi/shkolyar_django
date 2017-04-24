# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(default='model', max_length=55)),
                ('counter', models.IntegerField(default=1)),
                ('uri', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'view_count',
            },
        ),
    ]