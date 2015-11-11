# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0038_auto_20150919_2351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positioninunit',
            name='phone',
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='phone',
            field=models.ManyToManyField(blank=True, verbose_name='Телефон', to='phones.Phone'),
        ),
    ]
