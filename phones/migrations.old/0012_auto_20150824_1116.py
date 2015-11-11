# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0011_unit_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='slug',
            field=models.SlugField(verbose_name='Ссылка', max_length=255, blank=True),
        ),
    ]
