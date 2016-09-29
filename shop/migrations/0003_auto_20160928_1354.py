# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20160928_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[(10, 'Печенье'), (2, 'Капкейк'), (3, 'Торт')]),
        ),
    ]
