# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[(1, 'Печенье'), (2, 'Капкейк'), (3, 'Торт')]),
        ),
    ]
