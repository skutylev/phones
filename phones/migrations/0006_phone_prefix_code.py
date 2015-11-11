# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_phone_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='prefix_code',
            field=models.CharField(verbose_name='Префикс', default='246-05-55', max_length=5, choices=[('246-05-55', '246-05-55'), ('600-8', '600-8'), ('210-0', '210-0')]),
        ),
    ]
