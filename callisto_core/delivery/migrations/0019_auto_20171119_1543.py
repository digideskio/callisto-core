# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0018_remove_matchreport_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchreport',
            name='encode_prefix',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='matchreport',
            name='salt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='encode_prefix',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='salt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sentreport',
            name='to_address',
            field=models.TextField(),
        ),
    ]
