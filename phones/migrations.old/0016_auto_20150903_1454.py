# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0015_auto_20150902_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.ManyToManyField(to='phones.Phone', related_name='phone', blank=True, verbose_name='Телефон'),
        ),
    ]
