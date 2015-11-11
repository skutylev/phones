# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0016_auto_20150903_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ForeignKey(blank=True, related_name='address', verbose_name='Адрес', to='phones.Address'),
        ),
    ]
