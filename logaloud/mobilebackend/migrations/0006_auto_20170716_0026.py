# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilebackend', '0005_auto_20170715_2044'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Connection',
            new_name='BConnection',
        ),
        migrations.AlterField(
            model_name='listing',
            name='listing_type',
            field=models.CharField(choices=[(b'Normal', b'Normal'), (b'Ally', b'Ally'), (b'Admin_test', b'Admin_test'), (b'Great Perks', b'Great Perks')], max_length=100),
        ),
    ]
