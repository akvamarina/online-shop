# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import shop.models
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_auto_20160929_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('token', models.CharField(default=shop.models.Cart.generate_token, max_length=40)),
                ('total_price', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(default=datetime.datetime(2016, 9, 29, 17, 27, 39, 872336, tzinfo=utc))),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(to='shop.Cart')),
                ('product', models.ForeignKey(to='shop.Product')),
            ],
        ),
    ]
