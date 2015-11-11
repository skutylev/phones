# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0028_auto_20150919_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positioninunit',
            name='chief',
        ),
        migrations.AddField(
            model_name='person',
            name='chief',
            field=models.ForeignKey(blank=True, related_name='subordinates', to='phones.Person', verbose_name='Руководитель', null=True),
        ),
    ]
