# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-06-12 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winapi', '0004_auto_20170612_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='dll',
            name='win10',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dll',
            name='win7',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dll',
            name='win8',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dll',
            name='winxp',
            field=models.BooleanField(default=False),
        ),
    ]
