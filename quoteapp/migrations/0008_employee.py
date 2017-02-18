# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-16 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quoteapp', '0007_remove_quotemodel_quser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userquotes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quoteapp.QuoteModel')),
            ],
        ),
    ]