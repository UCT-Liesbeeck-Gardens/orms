# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flat_number', models.CharField(max_length=10)),
                ('student_number', models.CharField(max_length=10)),
                ('mobile_number', models.CharField(max_length=20)),
                ('email_address', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('data_of_application', models.DateTimeField(verbose_name=b'date applied')),
            ],
        ),
    ]
