# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0023_unit_unit_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='edu',
        ),
        migrations.AddField(
            model_name='person',
            name='edu',
            field=models.ForeignKey(verbose_name='Образование', blank=True, to='phones.Edu', default=1),
            preserve_default=False,
        ),
    ]
