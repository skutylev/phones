# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0036_auto_20150919_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninunit',
            name='address',
            field=models.ForeignKey(blank=True, verbose_name='Адрес', to='phones.Address'),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='phone',
            field=models.ForeignKey(blank=True, verbose_name='Телефон', to='phones.Phone'),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='position',
            field=models.ForeignKey(blank=True, verbose_name='Должность', to='phones.Position'),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='unit',
            field=models.ForeignKey(blank=True, verbose_name='Подразделение', to='phones.Unit'),
        ),
    ]
