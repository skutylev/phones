# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0041_auto_20150920_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='unit',
            field=models.ManyToManyField(blank=True, verbose_name='Подразделение', related_name='units', to='phones.Unit'),
        ),
        migrations.AlterField(
            model_name='person',
            name='work_hours',
            field=models.ForeignKey(blank=True, verbose_name='Часы работы', related_name='work_hours', to='phones.WorkHours'),
        ),
    ]
