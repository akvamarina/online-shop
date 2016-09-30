# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_productcart_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcart',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]
