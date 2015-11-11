# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0051_person_modify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='modify_date',
        ),
    ]
