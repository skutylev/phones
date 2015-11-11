# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0010_auto_20150823_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Ссылка', max_length=30),
        ),
    ]
