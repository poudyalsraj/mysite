# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170813_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
    ]
