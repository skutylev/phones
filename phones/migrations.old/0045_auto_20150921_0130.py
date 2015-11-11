# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0044_auto_20150921_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='work_hours',
            field=models.ForeignKey(verbose_name='Часы работы', related_name='work_hours', to='phones.WorkHours', blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='address',
            field=models.ForeignKey(verbose_name='Адрес', to='phones.Address', blank=True, default=1),
        ),
    ]
