# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_appownershiptransfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='apprelease',
            name='changelog',
            field=models.TextField(default='', help_text='The release changelog. Can contain Markdown', verbose_name='Changelog'),
        ),
    ]