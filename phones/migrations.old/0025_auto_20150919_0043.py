# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0024_auto_20150919_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='edu',
        ),
        migrations.AddField(
            model_name='edu',
            name='person',
            field=models.ForeignKey(to='phones.Person', default=1),
            preserve_default=False,
        ),
    ]
