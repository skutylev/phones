# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0046_auto_20150921_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='work_hours',
            field=models.ForeignKey(to='phones.WorkHours', verbose_name='Часы работы', blank=True, related_name='work_hours', default='6'),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='address',
            field=models.ForeignKey(to='phones.Address', verbose_name='Адрес', blank=True, default='10'),
        ),
    ]
