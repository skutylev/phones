# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0026_edu_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edu',
            name='key',
        ),
    ]
