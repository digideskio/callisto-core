# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0018_report_to_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matchreport',
            old_name='report',
            new_name='record',
        ),
        migrations.RenameField(
            model_name='sentfullreport',
            old_name='report',
            new_name='record',
        ),
    ]
