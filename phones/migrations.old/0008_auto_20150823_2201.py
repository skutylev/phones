# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_auto_20150823_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='authors',
        ),
        migrations.DeleteModel(
            name='Publication',
        ),
    ]
