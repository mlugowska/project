# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-05 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0006_auto_20170605_1845'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ('-carrots',)},
        ),
    ]
