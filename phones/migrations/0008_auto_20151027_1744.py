# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0007_auto_20151027_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='area',
            field=models.CharField(choices=[('495', '495'), ('499', '499'), ('925', '925')], default='495', verbose_name='Код города', max_length=15),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=16, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='prefix_code',
            field=models.CharField(choices=[('246-05-55', '246-05-55'), ('600-8', '600-8'), ('210-0', '210-0')], default='246-05-55', verbose_name='Префикс', max_length=15),
        ),
    ]
