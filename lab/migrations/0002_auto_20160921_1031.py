# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 10:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Books',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='lab.Author'),
            preserve_default=False,
        ),
    ]
