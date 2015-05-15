# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flat_floor', models.CharField(max_length=10)),
                ('flat_number', models.CharField(max_length=10)),
                ('room_number', models.CharField(max_length=10)),
                ('flat_type', models.CharField(max_length=10)),
                ('additional_info', models.CharField(max_length=100)),
            ],
        ),
    ]
