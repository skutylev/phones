# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0047_auto_20150921_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninunit',
            name='person',
            field=models.ForeignKey(null=True, blank=True, verbose_name='Пользователь', to='phones.Person'),
        ),
    ]
