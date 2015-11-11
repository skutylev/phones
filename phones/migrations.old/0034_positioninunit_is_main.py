# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0033_auto_20150919_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='positioninunit',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основное место работы'),
        ),
    ]
