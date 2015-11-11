# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_auto_20150823_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areacode',
            name='area_code',
            field=models.CharField(default='1', max_length=6, verbose_name='Код города'),
        ),
        migrations.AlterField(
            model_name='city',
            name='area_code',
            field=models.ManyToManyField(default='1', verbose_name='Код города', to='phones.AreaCode'),
        ),
        migrations.AlterField(
            model_name='city',
            name='city',
            field=models.CharField(default='1', max_length=10, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='postcode',
            name='post_code',
            field=models.CharField(default='1', max_length=6, verbose_name='Почтовый индекс'),
        ),
        migrations.AlterField(
            model_name='prefix',
            name='prefix',
            field=models.CharField(default='1', max_length=9, verbose_name='Префикс'),
        ),
        migrations.AlterField(
            model_name='street',
            name='post_code',
            field=models.ManyToManyField(default='1', verbose_name='Почтовый индекс', to='phones.PostCode'),
        ),
        migrations.AlterField(
            model_name='street',
            name='street',
            field=models.CharField(default='1', max_length=40, verbose_name='Улица'),
        ),
    ]
