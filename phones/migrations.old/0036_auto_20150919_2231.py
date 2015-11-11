# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0035_auto_20150919_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positioninunit',
            name='boss',
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='chief',
            field=models.ForeignKey(verbose_name='Руководитель', to='phones.Person', blank=True, null=True, related_name='subordinates'),
        ),
    ]
