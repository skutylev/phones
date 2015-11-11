# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0045_auto_20150921_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='work_hours',
            field=models.ForeignKey(blank=True, related_name='work_hours', verbose_name='Часы работы', default='1', to='phones.WorkHours'),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='address',
            field=models.ForeignKey(blank=True, verbose_name='Адрес', default='1', to='phones.Address'),
        ),
    ]
