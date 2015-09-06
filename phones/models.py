from django.db import models
from hashlib import md5
import os
from ckeditor.fields import RichTextField
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from phones.slugify import slugify
from sorl.thumbnail import ImageField


############################
# Автоматическая генерация #
# имени файла в ImageField #
############################

def get_person_image_path(instance, filename):
    filename = filename.encode('utf-8')
    hashname = md5(filename).hexdigest() + '.jpg'
    return os.path.join(hashname[:2], hashname[2:4],
                        hashname)

###########################
# Добавляем модели данных #
###########################

# Телефонные префиксы
class Prefix(models.Model):
    prefix = models.CharField(max_length=9, verbose_name='Префикс', default='1')

    def __str__(self):
        return self.prefix

    class Meta:
        verbose_name = 'Префикс'
        verbose_name_plural = 'Префиксы'
        ordering = ['prefix']

# Коды города
class AreaCode(models.Model):
    area_code = models.CharField(max_length=6, verbose_name='Код города', default='1')

    def __str__(self):
        return self.area_code

    class Meta:
        verbose_name = 'Код города'
        verbose_name_plural = 'Коды городов'
        ordering = ['area_code']

# Почтовые индексы
class PostCode(models.Model):
    post_code = models.CharField(max_length=6, verbose_name='Почтовый индекс', default='1')

    def __str__(self):
        return self.post_code

    class Meta:
        verbose_name = 'Почтовый индекс'
        verbose_name_plural = 'Почтовые индексы'
        ordering = ['post_code']
# Города
class City(models.Model):
    city = models.CharField(max_length=10, verbose_name='Город', default='1')
    area_code = models.ManyToManyField(AreaCode, verbose_name="Код города", default='1')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['city']

# Улицы
class Street(models.Model):
    street = models.CharField(max_length=40, verbose_name='Улица', default='1')
    post_code = models.ManyToManyField(PostCode, verbose_name="Почтовый индекс", default='1')

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['street']

# Здания
class Building(models.Model):
    building = models.CharField(max_length=5, verbose_name='Здание', default='1')

    def __str__(self):
        return self.building

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
        ordering = ['building']

# Корпуса в зданиях
class Campus(models.Model):
    campus = models.CharField(max_length=5, verbose_name='Корпус', default='1')
    prefix = models.ManyToManyField(Prefix, verbose_name='Префикс', default='1')

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

# Образование
class Edu(models.Model):
    EDU_CHOICES = (
        ('Бакалавриат', 'Бакалавриат'),
        ('Магистратура', 'Магистратура'),
        ('Аспирантура', 'Аспирантура'),
    )
    level = models.CharField(max_length=255, choices=EDU_CHOICES, verbose_name='Образование')
    university = models.CharField(max_length=255, verbose_name='Университет')
    faculty = models.CharField(max_length=255, verbose_name='Факультет')
    department = models.CharField(max_length=255, verbose_name='Кафедра')
    speciality = models.CharField(max_length=255, verbose_name='Специальность')
    graduate = models.DateField(verbose_name='Дата окончания')
    key = models.ForeignKey('self',)

    def get_absolute_url(self):
        return "/phones/%s/" % self.id

    def __str__(self):
          return u'%s: %s %s, %s, %s, %s' % (self.level, self.graduate, self.university, self.faculty, self.department, self.speciality)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'

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

# Справочник подразделений, с шифрами и иерархией
class Unit(MPTTModel, models.Model):
    unit_cypher = models.CharField(max_length=15, verbose_name='Шифр', blank=True)
    unit_name = models.CharField(max_length=200, verbose_name='Подразделение')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name='Родитель', db_index=True, )
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', blank=True)

    class MPTTMeta:
        level_attr = 'mptt_level'

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.unit_name)
        super(Unit, self).save(*args, **kwargs)
        Unit.objects.update()

    def get_acronym(self):
        return ''.join(e[0] for e in self.unit_name.split())

    def get_absolute_url(self):
        return "/phones/%s/" % self.slug

    def __str__(self):
        return self.unit_name

mptt.register(Unit,)

# Справочник должностей, с начальниками и подчиненными
class Position(models.Model):
    position = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['position']

# И наконец люди
class Person(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', blank=True, null=True, )
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, default='00.00.0000')
    email = models.EmailField(verbose_name='Email', blank=True)
    photo = models.ImageField(upload_to=get_person_image_path, verbose_name='Фотография', blank=True, default=None
                              )
    slug = models.SlugField(max_length=30, verbose_name='Ссылка', blank=True)
    unit = models.ManyToManyField(Unit, verbose_name='Подразделение', related_name='units')
    position = models.ManyToManyField(Position, verbose_name='Должность', related_name='positions', blank=True, null=True)
    edu = models.ManyToManyField(Edu, verbose_name='Образование', blank=True, null=True)
    degree = models.ForeignKey(Degree, verbose_name='Ученая степень', default='3', related_name='degrees')
    science_rank = models.ForeignKey(ScienceRank, verbose_name='Ученое звание', default='3', related_name='science_ranks')
    address = models.ForeignKey(Address, verbose_name='Адрес', related_name='address', blank=True, null=True)
    phone = models.ManyToManyField(Phone, verbose_name='Телефон', related_name='phone', blank=True)
    work_hours = models.ForeignKey(WorkHours, verbose_name='Часы работы', related_name='work_hours')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    publish = models.BooleanField(default=False, verbose_name='Опубликовано')
    chief = models.ForeignKey('self', verbose_name='Руководитель', blank=True, null=True, related_name='subordinates')

    def __str__(self):
        return u'%s %s.%s.' % (self.last_name, self.first_name[:1], self.middle_name[:1])

    def get_phones(self):
        return ',\n'.join([str(p) for p in self.phone.all()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name[:1] + self.middle_name[:1] + self.last_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def get_subordinates(self):
        subordinates = Person.objects.filter(chief_id=self.id)
        return subordinates

    def get_full_phone(self):
        full_phone = Person.phone.select_related('phone')
        return full_phone

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['-publish_date']