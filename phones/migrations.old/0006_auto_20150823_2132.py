# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_publication_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name_plural': 'Публикации', 'ordering': ['title'], 'verbose_name': 'Публикация'},
        ),
        migrations.AlterField(
            model_name='publication',
            name='lang',
            field=models.CharField(default=1, verbose_name='Язык публикации', max_length=255, choices=[('ru', 'Русский'), ('en', 'Английский'), ('de', 'Немецкий')]),
        ),
    ]
