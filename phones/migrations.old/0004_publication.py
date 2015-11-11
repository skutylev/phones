# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20150823_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название публикации')),
                ('lang', models.CharField(max_length=255, verbose_name='Язык публикации', choices=[('ru', 'Русский'), ('en', 'Английский'), ('de', 'Немецкий')])),
                ('authors', models.ManyToManyField(related_name='authors', verbose_name='Авторы', to='phones.Person')),
            ],
        ),
    ]
