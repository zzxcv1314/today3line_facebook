# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-05 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161105_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='parseddata',
            name='dirty',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]