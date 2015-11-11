# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phones.models
import ckeditor.fields
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['street', 'building', 'campus', 'office'],
                'verbose_name_plural': 'Адреса',
                'verbose_name': 'Адрес',
            },
        ),
        migrations.CreateModel(
            name='AreaCode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('area_code', models.CharField(default='1', max_length=6, verbose_name='Код города')),
            ],
            options={
                'ordering': ['area_code'],
                'verbose_name_plural': 'Коды городов',
                'verbose_name': 'Код города',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('building', models.CharField(default='1', max_length=5, verbose_name='Здание')),
            ],
            options={
                'ordering': ['building'],
                'verbose_name_plural': 'Здания',
                'verbose_name': 'Здание',
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('campus', models.CharField(default='1', max_length=5, verbose_name='Корпус')),
            ],
            options={
                'ordering': ['campus'],
                'verbose_name_plural': 'Корпуса',
                'verbose_name': 'Корпус',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('city', models.CharField(default='1', max_length=10, verbose_name='Город')),
                ('area_code', models.ManyToManyField(default='1', verbose_name='Код города', to='phones.AreaCode')),
            ],
            options={
                'ordering': ['city'],
                'verbose_name_plural': 'Города',
                'verbose_name': 'Город',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=50, verbose_name='Ученая степень')),
                ('short_degree', models.CharField(max_length=6, verbose_name='Сокращение')),
            ],
            options={
                'verbose_name_plural': 'Ученые степени',
                'verbose_name': 'Ученая степень',
            },
        ),
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('level', models.CharField(blank=True, max_length=255, verbose_name='Образование', choices=[('Бакалавриат', 'Бакалавриат'), ('Магистратура', 'Магистратура'), ('Аспирантура', 'Аспирантура'), ('ДПО', 'ДПО')])),
                ('university', models.CharField(blank=True, max_length=255, verbose_name='Университет')),
                ('faculty', models.CharField(blank=True, max_length=255, verbose_name='Факультет')),
                ('department', models.CharField(blank=True, max_length=255, verbose_name='Кафедра')),
                ('speciality', models.CharField(blank=True, max_length=255, verbose_name='Специальность')),
                ('graduate', models.DateField(blank=True, verbose_name='Дата окончания')),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Образования',
                'verbose_name': 'Образование',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('office', models.CharField(max_length=5, verbose_name='Кабинет')),
            ],
            options={
                'ordering': ['office'],
                'verbose_name_plural': 'Кабинеты',
                'verbose_name': 'Кабинет',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('org_name', models.CharField(max_length=100, verbose_name='Название организации')),
                ('short_org_name', models.CharField(max_length=10, verbose_name='Короткое название')),
                ('org_desc', ckeditor.fields.RichTextField(max_length=800, verbose_name='Описание')),
                ('logo', models.ImageField(blank=True, verbose_name='Логотип', upload_to=phones.models.get_person_image_path)),
                ('bank_details', models.CharField(max_length=50, verbose_name='Банковские реквизиты')),
                ('l_address', models.ForeignKey(max_length=200, verbose_name='Юридический адрес', to='phones.Address')),
            ],
            options={
                'ordering': ['org_name'],
                'verbose_name_plural': 'Организации',
                'verbose_name': 'Организация',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('middle_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('birthday', models.DateField(blank=True, default='00.00.0000', verbose_name='Дата рождения')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('photo', models.ImageField(blank=True, default=None, verbose_name='Фотография', upload_to=phones.models.get_person_image_path)),
                ('slug', models.SlugField(blank=True, max_length=30, verbose_name='Ссылка')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('publish', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('degree', models.ForeignKey(related_name='degrees', default='3', verbose_name='Ученая степень', to='phones.Degree')),
            ],
            options={
                'ordering': ['-publish_date'],
                'verbose_name_plural': 'Сотрудники',
                'verbose_name': 'Сотрудник',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('country_code', models.CharField(default='+7', max_length=2, verbose_name='Код страны')),
                ('number', models.CharField(max_length=6, verbose_name='Номер телефона')),
                ('is_outer', models.BooleanField(default=False, verbose_name='Внешний')),
                ('area_code', models.ForeignKey(to='phones.AreaCode')),
            ],
            options={
                'ordering': ['area_code'],
                'verbose_name_plural': 'Телефоны',
                'verbose_name': 'Телефон',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name_plural': 'Должности',
                'verbose_name': 'Должность',
            },
        ),
        migrations.CreateModel(
            name='PositionInUnit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_main', models.BooleanField(default=False, verbose_name='Основное место работы')),
                ('order', models.PositiveIntegerField()),
                ('address', models.ForeignKey(default='10', verbose_name='Адрес', blank=True, to='phones.Address')),
                ('chief', models.ForeignKey(related_name='subordinates', verbose_name='Руководитель', blank=True, to='phones.Person')),
                ('person', models.ForeignKey(null=True, verbose_name='Пользователь', blank=True, to='phones.Person')),
                ('phone', models.ManyToManyField(related_name='phones', blank=True, verbose_name='Телефон', to='phones.Phone')),
                ('position', models.ForeignKey(verbose_name='Должность', blank=True, to='phones.Position')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name_plural': 'Должности в подразделениях',
                'verbose_name': 'Должность в подразделении',
            },
        ),
        migrations.CreateModel(
            name='PostCode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('post_code', models.CharField(default='1', max_length=6, verbose_name='Почтовый индекс')),
            ],
            options={
                'ordering': ['post_code'],
                'verbose_name_plural': 'Почтовые индексы',
                'verbose_name': 'Почтовый индекс',
            },
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('prefix', models.CharField(default='1', max_length=9, verbose_name='Префикс')),
            ],
            options={
                'ordering': ['prefix'],
                'verbose_name_plural': 'Префиксы',
                'verbose_name': 'Префикс',
            },
        ),
        migrations.CreateModel(
            name='ScienceRank',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('science_rank', models.CharField(max_length=50, verbose_name='Ученое звание')),
                ('short_science_rank', models.CharField(max_length=6, verbose_name='Сокращение')),
            ],
            options={
                'verbose_name_plural': 'Ученые звания',
                'verbose_name': 'Ученое звание',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('street', models.CharField(default='1', max_length=40, verbose_name='Улица')),
                ('post_code', models.ManyToManyField(default='1', verbose_name='Почтовый индекс', to='phones.PostCode')),
            ],
            options={
                'ordering': ['street'],
                'verbose_name_plural': 'Улицы',
                'verbose_name': 'Улица',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('unit_cypher', models.CharField(blank=True, max_length=15, verbose_name='Шифр')),
                ('unit_name', models.CharField(blank=True, max_length=200, verbose_name='Подразделение')),
                ('unit_short_name', models.CharField(blank=True, max_length=255, verbose_name='Сокращение')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Ссылка')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', null=True, verbose_name='Родитель', blank=True, to='phones.Unit')),
            ],
            options={
                'verbose_name_plural': 'Подразделения',
                'verbose_name': 'Подразделение',
            },
        ),
        migrations.CreateModel(
            name='WorkHours',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('begin_hours', models.TimeField(verbose_name='Начало рабочего дня')),
                ('end_hours', models.TimeField(verbose_name='Конец рабочего дня')),
            ],
            options={
                'ordering': ['begin_hours'],
                'verbose_name_plural': 'Часы работы',
                'verbose_name': 'Часы работы',
            },
        ),
        migrations.AddField(
            model_name='positioninunit',
            name='unit',
            field=models.ForeignKey(verbose_name='Подразделение', blank=True, to='phones.Unit'),
        ),
        migrations.AddField(
            model_name='phone',
            name='prefix',
            field=models.ForeignKey(to='phones.Prefix'),
        ),
        migrations.AddField(
            model_name='person',
            name='science_rank',
            field=models.ForeignKey(related_name='science_ranks', default='3', verbose_name='Ученое звание', to='phones.ScienceRank'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(null=True, verbose_name='Пользователь', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='work_hours',
            field=models.ForeignKey(related_name='work_hours', default='6', verbose_name='Часы работы', blank=True, to='phones.WorkHours'),
        ),
        migrations.AddField(
            model_name='edu',
            name='person',
            field=models.ForeignKey(to='phones.Person', verbose_name='Сотрудник'),
        ),
        migrations.AddField(
            model_name='campus',
            name='prefix',
            field=models.ManyToManyField(default='1', verbose_name='Префикс', to='phones.Prefix'),
        ),
        migrations.AddField(
            model_name='address',
            name='building',
            field=models.ForeignKey(to='phones.Building'),
        ),
        migrations.AddField(
            model_name='address',
            name='campus',
            field=models.ForeignKey(to='phones.Campus'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(to='phones.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='office',
            field=models.ForeignKey(to='phones.Office'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(to='phones.Street'),
        ),
    ]
