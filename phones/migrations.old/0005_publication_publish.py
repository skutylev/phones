# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='publish',
            field=models.BooleanField(verbose_name='Опубликовано', default=False),
        ),
    ]
