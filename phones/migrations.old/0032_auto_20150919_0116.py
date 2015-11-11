# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0031_auto_20150919_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninunit',
            name='position',
            field=models.ForeignKey(verbose_name='Должность', to='phones.Position'),
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='unit',
            field=models.ForeignKey(verbose_name='Подразделение', to='phones.Unit'),
        ),
    ]
