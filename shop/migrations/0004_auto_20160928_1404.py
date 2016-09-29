# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160928_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[(0, 'Печенье'), (1, 'Капкейк'), (2, 'Торт')]),
        ),
    ]
