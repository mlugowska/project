# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-26 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_profile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='carrot',
            new_name='carrots',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
