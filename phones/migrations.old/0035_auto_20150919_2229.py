# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0034_positioninunit_is_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='chief',
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='boss',
            field=models.ForeignKey(to='phones.Person', default=1, related_name='positioninunit_boss'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='positioninunit',
            name='person',
            field=models.ForeignKey(to='phones.Person'),
        ),
    ]
