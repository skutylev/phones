# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phones.models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0012_auto_20150824_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='edu',
            field=models.ManyToManyField(verbose_name='Образование', to='phones.Edu', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(verbose_name='Фотография', upload_to=phones.models.get_person_image_path, blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.CharField(max_length=100, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_name',
            field=models.CharField(max_length=200, verbose_name='Подразделение'),
        ),
    ]
