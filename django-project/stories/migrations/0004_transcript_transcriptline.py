# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20170531_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='For your use. Not displayed to users.', max_length=1024, verbose_name='Transcript Name')),
                ('type', models.IntegerField(choices=[(0, 'Normal'), (1, 'Smart')], default=0, help_text='Smart transcripts include timecodes and follow along with audio.', verbose_name='Transcript Type')),
                ('text', models.TextField(blank=True, help_text='Markdown version of your transcript. Optional for smart.', verbose_name='Transcript Text')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TranscriptLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speaker', models.CharField(max_length=140, verbose_name='Speaker Display Name')),
                ('text', models.TextField(help_text='What the speaker says. Markdown compatible.', verbose_name='Text')),
                ('tc_min', models.IntegerField(default=0, verbose_name='Minutes')),
                ('tc_sec', models.IntegerField(verbose_name='Seconds')),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', related_query_name='line', to='stories.Transcript')),
            ],
            options={
                'ordering': ['tc_min', 'tc_sec'],
            },
        ),
    ]