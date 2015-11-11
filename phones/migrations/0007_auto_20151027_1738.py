# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_phone_prefix_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'Телефон', 'verbose_name_plural': 'Телефоны', 'ordering': ['area']},
        ),
        migrations.RemoveField(
            model_name='phone',
            name='area_code',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='is_mobile',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='is_outer',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='prefix',
        ),
    ]
