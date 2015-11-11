# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0021_auto_20150914_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='is_outer',
            field=models.BooleanField(verbose_name='Внешний', default=False),
        ),
    ]
