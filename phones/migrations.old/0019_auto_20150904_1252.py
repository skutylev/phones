# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0018_auto_20150904_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.ManyToManyField(null=True, to='phones.Position', blank=True, verbose_name='Должность', related_name='positions'),
        ),
    ]
