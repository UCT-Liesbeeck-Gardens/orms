# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flat_number', models.CharField(max_length=10)),
                ('room_number', models.CharField(max_length=10)),
                ('flat_type', models.CharField(max_length=10)),
                ('additional_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='flat_floor',
            field=models.ForeignKey(to='rooms.Floor'),
        ),
    ]
