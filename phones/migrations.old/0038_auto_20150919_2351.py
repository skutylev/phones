# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0037_auto_20150919_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='department',
            field=models.CharField(blank=True, max_length=255, verbose_name='Кафедра'),
        ),
        migrations.AlterField(
            model_name='edu',
            name='faculty',
            field=models.CharField(blank=True, max_length=255, verbose_name='Факультет'),
        ),
        migrations.AlterField(
            model_name='edu',
            name='graduate',
            field=models.DateField(blank=True, verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='edu',
            name='level',
            field=models.CharField(blank=True, max_length=255, choices=[('Бакалавриат', 'Бакалавриат'), ('Магистратура', 'Магистратура'), ('Аспирантура', 'Аспирантура')], verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='edu',
            name='speciality',
            field=models.CharField(blank=True, max_length=255, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='edu',
            name='university',
            field=models.CharField(blank=True, max_length=255, verbose_name='Университет'),
        ),
    ]
