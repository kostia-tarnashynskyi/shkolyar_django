# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models
import unixtimestampfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextbookBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
                ('update_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('public_time', unixtimestampfield.fields.UnixTimeStampField(default=1493058114)),
                ('author', models.CharField(max_length=500)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('properties', models.TextField(blank=True, null=True)),
                ('lang', models.CharField(blank=True, max_length=2, null=True)),
                ('edition', models.CharField(blank=True, max_length=255, null=True)),
                ('isbn', models.CharField(blank=True, max_length=255, null=True)),
                ('format', models.CharField(blank=True, max_length=255, null=True)),
                ('public', models.BooleanField()),
                ('issue_id', models.TextField(blank=True, null=True)),
                ('issue_embed', models.TextField(blank=True, null=True)),
                ('vk_publish_time', unixtimestampfield.fields.UnixTimeStampField(default=0.0)),
                ('img', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('is_promote', models.BooleanField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('uri', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'textbook_book',
            },
            bases=(models.Model, main.models.ViewCounterModel),
        ),
        migrations.CreateModel(
            name='TextbookClas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('uri', models.CharField(max_length=255, unique=True)),
                ('create_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
                ('update_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=2, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_promote', models.BooleanField()),
            ],
            options={
                'db_table': 'textbook_clas',
            },
        ),
        migrations.CreateModel(
            name='TextbookSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('uri', models.CharField(max_length=255, unique=True)),
                ('create_time', unixtimestampfield.fields.UnixTimeStampField(auto_now_add=True)),
                ('update_time', unixtimestampfield.fields.UnixTimeStampField(auto_now=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('is_promote', models.BooleanField()),
                ('textbook_clas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='clas_subjects', to='textbook.TextbookClas')),
            ],
            options={
                'db_table': 'textbook_subject',
            },
        ),
        migrations.AddField(
            model_name='textbookbook',
            name='textbook_clas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='clas_textbooks', to='textbook.TextbookClas'),
        ),
        migrations.AddField(
            model_name='textbookbook',
            name='textbook_subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='subject_textbooks', to='textbook.TextbookSubject'),
        ),
    ]