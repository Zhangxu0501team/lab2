# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_auto_20160921_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.FloatField(),
        ),
    ]