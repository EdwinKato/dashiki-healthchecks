# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20170705_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='level',
            field=models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')]),
        ),
    ]
