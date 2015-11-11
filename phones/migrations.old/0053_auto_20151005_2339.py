# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0052_remove_person_modify_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positioninunit',
            name='phone',
            field=models.ManyToManyField(blank=True, to='phones.Phone', related_name='phones', verbose_name='Телефон'),
        ),
    ]
