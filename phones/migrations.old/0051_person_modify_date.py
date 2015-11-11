# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0050_auto_20150925_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='modify_date',
            field=django_extensions.db.fields.ModificationDateTimeField(default=1, auto_now=True),
            preserve_default=False,
        ),
    ]
