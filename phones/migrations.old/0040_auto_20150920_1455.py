# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0039_auto_20150920_1126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positioninunit',
            options={'verbose_name': 'Должность', 'ordering': ['order']},
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_name',
            field=models.CharField(verbose_name='Подразделение', blank=True, max_length=200),
        ),
    ]
