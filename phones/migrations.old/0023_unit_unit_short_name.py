# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0022_phone_is_outer'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='unit_short_name',
            field=models.CharField(verbose_name='Сокращение', max_length=255, blank=True),
        ),
    ]
