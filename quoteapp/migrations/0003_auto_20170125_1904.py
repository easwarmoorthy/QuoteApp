# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0002_auto_20170125_1715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quote',
            new_name='QuoteModel',
        ),
    ]
