# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_auto_20150823_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='edu',
            name='key',
            field=models.ForeignKey(default=1, to='phones.Edu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='edu',
            field=models.ManyToManyField(verbose_name='Образование', to='phones.Edu'),
        ),
    ]
