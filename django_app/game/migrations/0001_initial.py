# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('win', models.IntegerField(default=0)),
                ('lose', models.IntegerField(default=0)),
                ('draw', models.IntegerField(default=0)),
                ('win_rate', models.FloatField(default=0.0)),
                ('game_gap', models.FloatField(default=0.0)),
                ('recent_10_game', models.CharField(blank=True, max_length=10)),
                ('continuous', models.CharField(blank=True, max_length=5)),
                ('home_score', models.CharField(blank=True, max_length=10)),
                ('away_score', models.CharField(blank=True, max_length=10)),
                ('standard_date', models.CharField(max_length=32)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Team')),
            ],
        ),
    ]