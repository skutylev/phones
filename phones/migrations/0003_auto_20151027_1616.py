# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_auto_20151014_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='is_mobile',
            field=models.BooleanField(default=False, verbose_name='Мобильный'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='is_outer',
            field=models.BooleanField(default=False, verbose_name='Есть внешний'),
        ),
    ]
