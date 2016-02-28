# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0006_auto_20160227_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_field', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
