# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('purpose', models.TextField(null=True)),
                ('requires_power', models.BooleanField(default=False)),
                ('volts_required', models.DecimalField(null=True, max_digits=5, decimal_places=1)),
                ('mamps_required', models.IntegerField(null=True)),
                ('supplies_power', models.BooleanField(default=False)),
                ('volts_supplied', models.DecimalField(null=True, max_digits=5, decimal_places=1)),
                ('mamps_supplied', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(null=True)),
                ('manufact', models.CharField(max_length=128)),
                ('model_num', models.CharField(max_length=30)),
                ('device_type', models.CharField(choices=[('base', 'base'), ('structure', 'structure'), ('sensor', 'sensor'), ('indicator', 'indicator')], max_length=30)),
                ('manual', models.FileField(null=True, upload_to='')),
                ('picture', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='securitycomponent',
            name='device',
            field=models.ForeignKey(to='ss_zones.SecurityDevice'),
        ),
    ]
