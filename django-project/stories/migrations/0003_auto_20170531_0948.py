# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to=b'', verbose_name='Square Profile Photo'),
        ),
    ]