from django.db import models
###########################
# Добавляем модели данных #
###########################

# Справочник организаций
class Organization(models.Model):
    org_name = models.CharField(max_length=100, verbose_name=("Название организации"))
    short_org_name = models.CharField(max_length=10, verbose_name=("Короткое название"))
    org_desc = models.CharField(max_length=200, verbose_name=("Описание"))
    l_address = models.CharField(max_length=200, verbose_name=("Юридический адрес"))
    bank_details = models.CharField(max_length=50, verbose_name=("Банковские реквизиты"))

    def __str__(self):
        return self.short_org_name

# Справочник подразделений, с шифрами и иерархией
class Unit(models.Model):
    unit_cypher = models.CharField(max_length=10, verbose_name=("Шифр"))
    unit_name = models.CharField(max_length=100, verbose_name=("Подразделение"))
    unit_parent = models.CharField(max_length=100, verbose_name=("Родительское подразделение"))
    unit_child = models.CharField(max_length=100, verbose_name=("Дочернее подразделение"))

    def __str__(self):
        return self.unit_name

# Справочник должностей, с начальниками и подчиненными
class Position(models.Model):
    position = models.CharField(max_length=50, verbose_name=("Должность"))
    chief_position = models.CharField(max_length=50, verbose_name=("Начальник"))
    subordinate_position = models.CharField(max_length=50, verbose_name=("Подчиненные"))

    def __str__(self):
        return self.position

# Телефонные префиксы
class Prefix(models.Model):
    prefix = models.CharField(max_length=6, verbose_name=("Префикс"))

    def __str__(self):
        return self.prefix

# Коды города
class AreaCode(models.Model):
    area_code = models.CharField(max_length=6, verbose_name=("Код города"))

    def __str__(self):
        return self.area_code

# Почтовые индексы
class PostCode(models.Model):
    post_code = models.CharField(max_length=6, verbose_name=("Почтовый индекс"))

    def __str__(self):
        return self.post_code

# Города
class City(models.Model):
    city = models.CharField(max_length=10, verbose_name=("Город"))
    area_code = models.ForeignKey(AreaCode)

    def __str__(self):
        return self.city

# Улицы
class Street(models.Model):
    street = models.CharField(max_length=40, verbose_name=("Улица"))
    post_code = models.ForeignKey(PostCode)

    def __str__(self):
        return self.street

# Здания
class Building(models.Model):
    building = models.CharField(max_length=5, verbose_name=("Здание"))

    def __str__(self):
        return self.building

# Корпуса в зданиях
class Campus(models.Model):
    campus = models.CharField(max_length=5, verbose_name=("Корпус"))
    prefix = models.ForeignKey(Prefix)

    def __str__(self):
        return self.campus

# Кабинеты
class Office(models.Model):
    office = models.CharField(max_length=5, verbose_name=("Кабинет"))

    def __str__(self):
        return self.office

# Телефоны
class Phone(models.Model):
    country_code = models.CharField(max_length=2, verbose_name=("Код страны"))
    area_code = models.ForeignKey(AreaCode)
    prefix = models.ForeignKey(Prefix)
    number = models.CharField(max_length=6, verbose_name=("Номер телефона (внутр.)"))

    def __str__(self):
        return self.number

# Адреса
class Address(models.Model):
    city = models.ForeignKey(City)
    street = models.ForeignKey(Street)
    building = models.ForeignKey(Building)
    campus = models.ForeignKey(Campus)
    office = models.ForeignKey(Office)

# И наконец люди
class Person(models.Model):
    last_name = models.CharField(max_length=30, verbose_name=("Фамилия"))
    first_name = models.CharField(max_length=30, verbose_name=("Имя"))
    middle_name = models.CharField(max_length=30, verbose_name=("Отчество"))
    unit = models.ForeignKey(Unit)
    position = models.ForeignKey(Position)
    address = models.ForeignKey(Address)
    phone = models.ForeignKey(Phone)
    email = models.EmailField
