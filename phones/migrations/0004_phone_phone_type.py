# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20151027_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='phone_type',
            field=models.CharField(verbose_name='Тип', max_length=255, choices=[('0', 'Внутренний'), ('1', 'Внешний'), ('2', 'Мобильный')], default='0'),
        ),
    ]
