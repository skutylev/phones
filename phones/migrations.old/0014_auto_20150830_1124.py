# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0013_auto_20150826_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['-publish_date'], 'verbose_name': 'Сотрудник', 'verbose_name_plural': 'Сотрудники'},
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_cypher',
            field=models.CharField(verbose_name='Шифр', blank=True, max_length=15),
        ),
    ]
