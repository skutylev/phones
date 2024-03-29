from django.db import models
from hashlib import md5
import os
from ckeditor.fields import RichTextField
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User, AbstractUser
from phones.slugify import slugify
from django.db.models import Q
from sorl.thumbnail import ImageField
from django_select2 import Select2ChoiceField
import datetime
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added


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

class PostCode(models.Model):
    post_code = models.CharField(max_length=6, verbose_name='Почтовый индекс', default='1')

    def __str__(self):
        return self.post_code

    class Meta:
        verbose_name = 'Почтовый индекс'
        verbose_name_plural = 'Почтовые индексы'
        ordering = ['post_code']


class City(models.Model):
    city = models.CharField(max_length=10, verbose_name='Город', default='1')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['city']


class Street(models.Model):
    street = models.CharField(max_length=40, verbose_name='Улица', default='1')
    post_code = models.ManyToManyField(PostCode, verbose_name="Почтовый индекс", default='1')

    def __str__(self):
        return self.street

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ['street']


class Building(models.Model):
    building = models.CharField(max_length=5, verbose_name='Здание', default='1')

    def __str__(self):
        return self.building

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
        ordering = ['building']


class Campus(models.Model):
    campus = models.CharField(max_length=5, verbose_name='Корпус', default='1')

    def __str__(self):
        return self.campus

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпуса'
        ordering = ['campus']


class Office(models.Model):
    office = models.CharField(max_length=5, verbose_name='Кабинет')

    def __str__(self):
        return self.office

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'
        ordering = ['office']


class WorkHours(models.Model):
    begin_hours = models.TimeField(verbose_name='Начало рабочего дня')
    end_hours = models.TimeField(verbose_name='Конец рабочего дня')

    def __str__(self):
        return u'%s-%s' % (self.begin_hours, self.end_hours)

    class Meta:
        verbose_name = 'Часы работы'
        verbose_name_plural = 'Часы работы'
        ordering = ['begin_hours']


class Phone(models.Model):
    TYPE_CHOICES = (
        ('0', 'Внутренний'),
        ('1', 'Внешний'),
        ('2', 'Мобильный'),
    )
    AREA_CODE_CHOICES = (
        ('495', '495'),
        ('499', '499'),
        ('925', '925'),
    )
    PREFIX_CHOICES = (
        ('246-05-55', '246-05-55'),
        ('600-8', '600-8'),
        ('210-0', '210-0'),
    )

    country_code = models.CharField(max_length=2, verbose_name='Код страны', default='+7',)
    area_code = models.CharField(max_length=15, choices=AREA_CODE_CHOICES, verbose_name='Код города', default='495')
    prefix = models.CharField(max_length=15, choices=PREFIX_CHOICES, verbose_name='Префикс', default='246-05-55')
    number = models.CharField(max_length=16, verbose_name='Номер телефона')
    phone_type = models.CharField(max_length=255, choices=TYPE_CHOICES, verbose_name='Тип', default='0')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        ordering = ['phone_type']


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
        ordering = ['street', 'building', 'campus', 'office']


class Degree(models.Model):
    degree = models.CharField(max_length=50, verbose_name='Ученая степень')
    short_degree = models.CharField(max_length=6, verbose_name='Сокращение')

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = 'Ученая степень'
        verbose_name_plural = 'Ученые степени'


class ScienceRank(models.Model):
    science_rank = models.CharField(max_length=50, verbose_name='Ученое звание')
    short_science_rank = models.CharField(max_length=6, verbose_name='Сокращение')

    def __str__(self):
        return self.science_rank

    class Meta:
        verbose_name = 'Ученое звание'
        verbose_name_plural = 'Ученые звания'


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


class Unit(MPTTModel, models.Model):
    unit_cypher = models.CharField(max_length=15, verbose_name='Шифр', blank=True)
    unit_name = models.CharField(max_length=200, verbose_name='Подразделение', blank=True)
    unit_short_name = models.CharField(max_length=255, verbose_name='Сокращение', blank=True)
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
        return "/units/%s/" % self.slug

    def __str__(self):
        return self.unit_name
mptt.register(Unit,)


class Position(models.Model):
    position = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['position']


class PositionInUnit(models.Model):
    person = models.ForeignKey('Person', verbose_name='Пользователь', blank=True, null=True, )
    unit = models.ForeignKey(Unit, verbose_name='Подразделение', blank=True)
    position = models.ForeignKey(Position, verbose_name='Должность', blank=True)
    phone = models.ManyToManyField(Phone, verbose_name='Телефон', related_name='phones', blank=True)
    address = models.ForeignKey(Address, verbose_name='Адрес', blank=True, default='10')
    chief = models.ForeignKey('Person', verbose_name='Руководитель', blank=True,  related_name='subordinates')
    is_main = models.BooleanField(default=False, verbose_name='Основное место работы', blank=True,)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Должность в подразделении'
        verbose_name_plural = 'Должности в подразделениях'
        ordering = ['order']

    def __str__(self):
        return u'%s / %s' % (self.position, self.unit)


class Person(models.Model):
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='profile', blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    middle_name = models.CharField(max_length=30, verbose_name='Отчество')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, default='00.00.0000')
    email = models.EmailField(verbose_name='Email', blank=True)
    photo = models.ImageField(upload_to=get_person_image_path, verbose_name='Фотография', blank=True, default=None)
    slug = models.SlugField(max_length=30, verbose_name='Ссылка', blank=True)
    degree = models.ForeignKey(Degree, verbose_name='Ученая степень', default='3', related_name='degrees')
    science_rank = models.ForeignKey(ScienceRank, verbose_name='Ученое звание', default='3', related_name='science_ranks')
    work_hours = models.ForeignKey(WorkHours, verbose_name='Часы работы', related_name='work_hours', blank=True, default='6')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    # modified_date = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False, verbose_name='Опубликовано')

    def get_unit(self):
        try:
            unit = PositionInUnit.objects.filter(person=self.id).select_related('unit__unit_name').values('unit__unit_name')[0].get('unit__unit_name')
            return unit
        except:
            return 'unit do not exist'

    def __str__(self):
        return u'%s %s.%s.' % (self.last_name, self.first_name[:1], self.middle_name[:1])

    def get_first_phone_main(self):
        return PositionInUnit.objects.filter(person=self.id).select_related('phone__number').values('phone__number')[0].get('phone__number')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name[:1] + self.middle_name[:1] + self.last_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def get_full_phone(self):
        full_phone = Person.phone.select_related('phone')
        return full_phone

    def birthday_soon(self):
        days_to_date = self.birthday.day - datetime.date.today().day
        months_to_date = self.birthday.month - datetime.date.today().month
        years_to_date = self.birthday.year - datetime.date.today().year
        if months_to_date == 0 and days_to_date == 1 and years_to_date >= 50 and years_to_date % 5 == 0:
            return 'Завтра %s %s празднует Юбилей' % (self.first_name, self.middle_name)
        elif months_to_date == 0 and days_to_date == 1:
            return 'Завтра %s %s празднует День рождения' % (self.first_name, self.middle_name)
        elif months_to_date == 0 and days_to_date == 0 and years_to_date >= 50 and years_to_date % 5 == 0:
            return 'Сегодня %s %s празднует Юбилей' % (self.first_name, self.middle_name)
        elif months_to_date == 0 and days_to_date == 0:
            return 'Сегодня %s %s празднует День рождения' % (self.first_name, self.middle_name)
        else:
            return False


    # @receiver(social_account_added)
    # def connect_with_sociallogin(self, *args, **kwargs):
    #     if self.email == request.user.email or self.last_name == request.user.last_name and self.first_name == request.user.given_name:
    #         self.user = request.user.name
    #         super().update(*args, **kwargs)


    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['last_name']


class Edu(models.Model):
    EDU_CHOICES = (
        ('Бакалавриат', 'Бакалавриат'),
        ('Магистратура', 'Магистратура'),
        ('Аспирантура', 'Аспирантура'),
        ('ДПО', 'ДПО'),
    )
    person = models.ForeignKey('Person', verbose_name='Сотрудник')
    level = models.CharField(max_length=255, choices=EDU_CHOICES, verbose_name='Образование', blank=True)
    university = models.CharField(max_length=255, verbose_name='Университет', blank=True)
    faculty = models.CharField(max_length=255, verbose_name='Факультет', blank=True)
    department = models.CharField(max_length=255, verbose_name='Кафедра', blank=True)
    speciality = models.CharField(max_length=255, verbose_name='Специальность', blank=True)
    graduate = models.DateField(verbose_name='Дата окончания', blank=True)
    test = models.CharField
    order = models.PositiveIntegerField()

    def __str__(self):
          return u'%s: %s %s, %s, %s, %s' % (self.level, self.graduate, self.university, self.faculty, self.department, self.speciality)

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образования'
