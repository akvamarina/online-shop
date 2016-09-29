# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20160929_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(unique=True, choices=[(0, 'Печенье'), (1, 'Капкейк'), (2, 'Торт')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='shop.Category', to_field='name'),
        ),
    ]
