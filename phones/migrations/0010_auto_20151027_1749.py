# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0009_auto_20151027_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campus',
            name='prefix',
        ),
        migrations.RemoveField(
            model_name='city',
            name='area_code',
        ),
        migrations.DeleteModel(
            name='AreaCode',
        ),
        migrations.DeleteModel(
            name='Prefix',
        ),
    ]
