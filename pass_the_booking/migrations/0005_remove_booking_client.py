# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pass_the_booking', '0004_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='client',
        ),
    ]
