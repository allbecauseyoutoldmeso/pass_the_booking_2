# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 10:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pass_the_booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='mobile',
            new_name='telephone',
        ),
    ]
