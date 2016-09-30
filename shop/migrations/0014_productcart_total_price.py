# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20160930_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcart',
            name='total_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
