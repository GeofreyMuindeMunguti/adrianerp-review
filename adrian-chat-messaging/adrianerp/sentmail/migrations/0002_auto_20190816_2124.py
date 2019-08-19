# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-16 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentmail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentemail',
            name='message',
            field=models.CharField(default='No Message', max_length=5000),
        ),
        migrations.AddField(
            model_name='sentemail',
            name='subject',
            field=models.CharField(default='No Subject', max_length=255),
        ),
    ]