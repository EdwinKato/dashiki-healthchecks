# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-12 14:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20170711_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='nag',
        ),
        migrations.AlterField(
            model_name='check',
            name='nag_time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]
