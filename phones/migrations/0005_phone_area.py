# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_phone_phone_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='area',
            field=models.CharField(choices=[('495', '495'), ('499', '499'), ('925', '925')], max_length=5, verbose_name='Код города', default='495'),
        ),
    ]
