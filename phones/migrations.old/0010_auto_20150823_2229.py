# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0009_auto_20150823_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='building',
            field=models.CharField(max_length=5, default='1', verbose_name='Здание'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus',
            field=models.CharField(max_length=5, default='1', verbose_name='Корпус'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='prefix',
            field=models.ManyToManyField(default='1', verbose_name='Префикс', to='phones.Prefix'),
        ),
    ]
