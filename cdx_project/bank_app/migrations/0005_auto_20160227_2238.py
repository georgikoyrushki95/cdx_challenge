# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0004_auto_20160227_2150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='user_profile',
        ),
        migrations.RemoveField(
            model_name='emergencymessage',
            name='user',
        ),
        migrations.AddField(
            model_name='emergencymessage',
            name='user_profile',
            field=models.ForeignKey(default='', to='bank_app.UserProfile'),
            preserve_default=False,
        ),
    ]
