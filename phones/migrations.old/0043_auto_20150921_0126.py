# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0042_auto_20150921_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninunit',
            name='person',
            field=models.ForeignKey(to='phones.Person', blank=True),
        ),
    ]
