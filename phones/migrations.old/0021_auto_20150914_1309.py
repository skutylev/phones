# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0020_auto_20150911_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ManyToManyField(verbose_name='Адрес', related_name='address', to='phones.Address', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='edu',
            field=models.ManyToManyField(verbose_name='Образование', to='phones.Edu', blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.ManyToManyField(verbose_name='Должность', related_name='positions', to='phones.Position', blank=True),
        ),
    ]
