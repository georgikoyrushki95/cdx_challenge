# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0005_auto_20160227_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user_profile',
            new_name='user',
        ),
    ]
