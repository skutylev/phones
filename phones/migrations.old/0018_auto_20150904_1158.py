# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0017_auto_20150904_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ForeignKey(related_name='address', null=True, to='phones.Address', blank=True, verbose_name='Адрес'),
        ),
    ]
