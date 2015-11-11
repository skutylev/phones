# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0032_auto_20150919_0116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positioninunit',
            options={'ordering': ['order'], 'verbose_name': ' '},
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='address',
            field=models.ForeignKey(default=1, verbose_name='Адрес', to='phones.Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='phone',
            field=models.ForeignKey(default=1, verbose_name='Телефон', to='phones.Phone'),
            preserve_default=False,
        ),
    ]
