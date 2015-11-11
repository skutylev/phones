# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0019_auto_20150904_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.ManyToManyField(to='phones.Address', verbose_name='Адрес', blank=True, null=True, related_name='address'),
        ),
    ]
