# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0003_auto_20170121_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lostads',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
