# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20160930_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
