# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0027_remove_edu_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionInUnit',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='chief',
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='chief',
            field=models.ForeignKey(to='phones.Person', related_name='chief'),
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='person',
            field=models.ForeignKey(to='phones.Person', related_name='person'),
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='position',
            field=models.ForeignKey(to='phones.Position'),
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='unit',
            field=models.ForeignKey(to='phones.Unit'),
        ),
    ]
