# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personinunit',
            name='person',
        ),
        migrations.RemoveField(
            model_name='personinunit',
            name='position',
        ),
        migrations.RemoveField(
            model_name='personinunit',
            name='unit',
        ),
        migrations.AlterField(
            model_name='person',
            name='unit',
            field=models.ManyToManyField(to='phones.Unit', related_name='units', verbose_name='Подразделение'),
        ),
        migrations.DeleteModel(
            name='PersonInUnit',
        ),
    ]
