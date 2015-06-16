# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20150612_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='floor',
            field=models.IntegerField(unique=True),
        ),
    ]
