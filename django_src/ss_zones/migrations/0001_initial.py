# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(null=True)),
                ('manufact', models.CharField(max_length=128)),
                ('model_num', models.CharField(max_length=30)),
                ('device_type', models.CharField(max_length=30, choices=[('base', 'base'), ('structure', 'structure'), ('sensor', 'sensor'), ('indicator', 'indicator')])),
                ('manual', models.FileField(upload_to='', null=True)),
                ('picture', models.ImageField(upload_to='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('purpose', models.TextField(null=True)),
                ('requires_power', models.BooleanField(default=False)),
                ('volts_required', models.DecimalField(max_digits=5, decimal_places=1, null=True)),
                ('mamps_required', models.IntegerField(null=True)),
                ('supplies_power', models.BooleanField(default=False)),
                ('volts_supplied', models.DecimalField(max_digits=5, decimal_places=1, null=True)),
                ('mamps_supplied', models.IntegerField(null=True)),
                ('device', models.ForeignKey(to='ss_zones.Device')),
            ],
        ),
    ]
