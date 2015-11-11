# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0048_auto_20150921_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Адреса', 'ordering': ['street', 'building', 'campus', 'office'], 'verbose_name': 'Адрес'},
        ),
    ]
