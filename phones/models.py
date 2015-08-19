from django.db import models
from hashlib import md5
import os
from time import time
from ckeditor.fields import RichTextField
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from phones.slugify import slugify
from sorl.thumbnail import ImageField
from django.utils.encoding import force_text as force_unicode

###########################
# Добавляем модели данных #
###########################

# Справочник подразделений, с шифрами и иерархией


class Unit(MPTTModel):
    unit_cypher = models.CharField(max_length=10, verbose_name='Шифр', blank=True)
    unit_name = models.CharField(max_length=100, verbose_name='Подразделение')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='Родитель', db_index=True, )
   # order = models.IntegerField(verbose_name='Порядок', default=1)

    class MPTTMeta:
     #   order_insertion_by = ['order']
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def save(self, *args, **kwargs):
        super(Unit, self).save(*args, **kwargs)
        Unit.objects.update()

    def __str__(self):
        return self.unit_name

mptt.register(Unit,)

# Справочник должностей, с начальниками и подчиненными
class Position(models.Model):
    position = models.CharField(max_length=50, verbose_name='Должность')
    chief_position = models.CharField(max_length=50, verbose_name='Начальник', blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['position']

# Телефонные префиксы
class Prefix(models.Model):
    prefix = models.CharField(max_length=9, verbose_name='Префикс')

    def __str__(self):
        return self.prefix

    class Meta:
        verbose_name = 'Префикс'
        verbose_name_plural = 'Префиксы'
        ordering = ['prefix']

# Коды города
class AreaCode(models.Model):
    area_code = models.CharField(max_length=6, verbose_name='Код города')

    def __str__(self):
        return self.area_code

    class Meta:
        verbose_name = 'Код города'
        verbose_name_plural = 'Коды городов'
        ordering = ['area_code']

# Почтовые индексы
class PostCode(models.Model):
    post_code = models.CharField(max_length=6, verbose_name='Почтовый индекс')

    def __str__(self):
        return self.post_code

    class Meta:
        verbose_name = 'Почтовый индекс'
        verbose_name_plural = 'Почтовые индексы'
        ordering = ['post_code']
# Города
class City(models.Model):
    city = models.CharField(max_length=10, verbose_name='Город')
    area_code = models.ManyToManyField(AreaCode, verbose_name="Код города")

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['city']

# Улицы
class Street(models.Model):
    street = models.CharField(max_length=40, verbose_name='Улица')
    post_code = models.ManyToManyField(PostCode, verbose_name="Почтовый индекс")

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['street']

# Здания
class Building(models.Model):
    building = models.CharField(max_length=5, verbose_name='Здание')

    def __str__(self):
        return self.building

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
        ordering = ['building']

# Корпуса в зданиях
class Campus(models.Model):
    campus = models.CharField(max_length=5, verbose_name='Корпус')
    prefix = models.ManyToManyField(Prefix, verbose_name='Префикс')

    def __str__(self):
        return self.campus

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'
        ordering = ['campus']

# Кабинеты
class Office(models.Model):
    office = models.CharField(max_length=5, verbose_name='Кабинет')

    def __str__(self):
        return self.office

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        ordering = ['office']

# Часы работы
class WorkHours(models.Model):
    begin_hours = models.TimeField(verbose_name='Начало рабочего дня')
    end_hours = models.TimeField(verbose_name='Конец рабочего дня')

    def __str__(self):
        return u'%s-%s' % (self.begin_hours, self.end_hours)

    class Meta:
        verbose_name = 'Часы работы'
        verbose_name_plural = 'Часы работы'
        ordering = ['begin_hours']

# Телефоны
class Phone(models.Model):
    country_code = models.CharField(max_length=2, verbose_name='Код страны', default='+7')
    area_code = models.ForeignKey(AreaCode)
    prefix = models.ForeignKey(Prefix)
    number = models.CharField(max_length=6, verbose_name='Номер телефона')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['area_code']

# Адреса
class Address(models.Model):
    city = models.ForeignKey(City)
    street = models.ForeignKey(Street)
    building = models.ForeignKey(Building)
    campus = models.ForeignKey(Campus)
    office = models.ForeignKey(Office)

    def __str__(self):
          return u'%s д. %s, %s-%s' % (self.street, self.building, self.campus, self.office)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ['street']

# Ученые степени
class Degree(models.Model):
    degree = models.CharField(max_length=50, verbose_name='Ученая степень')
    short_degree = models.CharField(max_length=6, verbose_name='Сокращение')

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'

# Ученые звания
class ScienceRank(models.Model):
    science_rank = models.CharField(max_length=50, verbose_name='Ученое звание')
    short_science_rank = models.CharField(max_length=6, verbose_name='Сокращение')

    def __str__(self):
        return self.science_rank

    class Meta:
        verbose_name = 'Ученое звание'
        verbose_name_plural = 'Ученые звания'

############################
# Автоматическая генерация #
# имени файла в ImageField #
############################


def get_person_image_path(instance, filename):
    filename = filename.encode('utf-8')
    hashname = md5(filename).hexdigest() + '.jpg'
    return os.path.join(hashname[:2], hashname[2:4],
                        hashname)

# Справочник организаций
class Organization(models.Model):
    org_name = models.CharField(max_length=100, verbose_name='Название организации')
    short_org_name = models.CharField(max_length=10, verbose_name='Короткое название')
    org_desc = RichTextField(max_length=800, verbose_name='Описание')
    logo = models.ImageField(upload_to=get_person_image_path, verbose_name='Логотип', blank=True)
    l_address = models.ForeignKey(Address, max_length=200, verbose_name='Юридический адрес')
    bank_details = models.CharField(max_length=50, verbose_name='Банковские реквизиты')

    def __str__(self):
        return self.short_org_name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['org_name']

# И наконец люди
class Person(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, default='00.00.0000')
    email = models.EmailField(verbose_name='Email', blank=True)
    photo = models.ImageField(upload_to=get_person_image_path, verbose_name='Фотография', blank=True, default='phones/images/default.jpg')
    slug = models.SlugField(max_length=30, verbose_name='Ссылка', blank=True)
    unit = models.ManyToManyField(Unit, verbose_name='Подразделение')
    position = models.ManyToManyField(Position, verbose_name='Должность')
    degree = models.ForeignKey(Degree, verbose_name='Ученая степень', default='3')
    science_rank = models.ForeignKey(ScienceRank, verbose_name='Ученое звание', default='3')
    address = models.ForeignKey(Address, verbose_name='Адрес')
    phone = models.ManyToManyField(Phone, verbose_name='Телефон')
    work_hours = models.ForeignKey(WorkHours, verbose_name='Часы работы')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    publish = models.BooleanField(default=False, verbose_name='Опубликовано')
    leader = models.ForeignKey('self', verbose_name='Руководитель', blank='True', null='True')

    def __str__(self):
        return u'%s %s.%s.' % (self.last_name, self.first_name[:1], self.middle_name[:1])

    def get_phones(self):
        return ',\n'.join([str(p) for p in self.phone.all()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name[:1] + self.middle_name[:1] + self.last_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return "/phones/%s/" % self.slug

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name']
