# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_auto_20151027_1744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name_plural': 'Телефоны', 'verbose_name': 'Телефон', 'ordering': ['phone_type']},
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='area',
            new_name='area_code',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='prefix_code',
            new_name='prefix',
        ),
    ]
