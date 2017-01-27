# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0004_auto_20170127_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotemodel',
            name='qname',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quotemodel',
            name='quote',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
