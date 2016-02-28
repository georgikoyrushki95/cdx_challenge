# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0007_testmessage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestMessage',
        ),
    ]
