# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 09:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0006_auto_20170216_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotemodel',
            name='quser',
        ),
    ]
