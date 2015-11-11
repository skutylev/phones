# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0030_positioninunit_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positioninunit',
            options={'verbose_name': 'Должность и подразделение', 'ordering': ['order']},
        ),
    ]
