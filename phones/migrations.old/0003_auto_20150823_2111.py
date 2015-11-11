# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20150823_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='chief',
        ),
        migrations.AddField(
            model_name='person',
            name='chief',
            field=models.ForeignKey(null=True, verbose_name='Руководитель', related_name='subordinates', to='phones.Person', blank=True),
        ),
    ]
