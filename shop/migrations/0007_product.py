# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20160928_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('photo', models.URLField()),
                ('price', models.PositiveIntegerField()),
                ('quantity_On_stock', models.PositiveIntegerField()),
                ('category', models.ForeignKey(to='shop.Category')),
            ],
        ),
    ]
