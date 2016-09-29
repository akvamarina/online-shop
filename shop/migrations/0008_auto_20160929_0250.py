# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity_On_stock',
            new_name='quantity_on_stock',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
