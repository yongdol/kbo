# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField(blank=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('contents', models.CharField(blank=True, max_length=500)),
                ('link', models.URLField(blank=True, unique=True)),
                ('img', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=10)),
                ('short_name', models.CharField(max_length=3)),
                ('nick_name', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Team'),
        ),
    ]
