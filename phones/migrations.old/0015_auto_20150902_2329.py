# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phones.models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0014_auto_20150830_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(upload_to=phones.models.get_person_image_path, verbose_name='Фотография', default=None, blank=True),
        ),
    ]
