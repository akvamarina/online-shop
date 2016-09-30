# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20160930_0404'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
