# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lostads',
            name='ads_created_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
