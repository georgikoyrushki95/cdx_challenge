# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank_app', '0006_auto_20160227_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emergencymessage',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='emergencymessage',
            name='user',
            field=models.ForeignKey(default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
