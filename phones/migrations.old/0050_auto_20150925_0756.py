# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0049_auto_20150921_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='address',
        ),
        migrations.RemoveField(
            model_name='person',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='person',
            name='position',
        ),
        migrations.RemoveField(
            model_name='person',
            name='unit',
        ),
    ]
