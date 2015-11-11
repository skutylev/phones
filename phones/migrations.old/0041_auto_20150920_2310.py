# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0040_auto_20150920_1455'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positioninunit',
            options={'verbose_name': 'Должность в подразделении', 'ordering': ['order'], 'verbose_name_plural': 'Должности в подразделениях'},
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='chief',
            field=models.ForeignKey(related_name='subordinates', verbose_name='Руководитель', to='phones.Person', blank=True, default=1),
            preserve_default=False,
        ),
    ]
