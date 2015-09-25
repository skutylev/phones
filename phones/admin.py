from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from phones.models import Organization, Unit, Position, Prefix, AreaCode, PostCode, City, Street, Building, Campus, Office, WorkHours, Phone, Address, Person, Degree, ScienceRank, Edu, PositionInUnit
from django.forms import ModelForm
from suit.widgets import EnclosedInput
from suit.admin import SortableStackedInline
from mptt.admin import MPTTModelAdmin
from import_export import resources
from django_select2 import AutoModelSelect2Field, AutoHeavySelect2Widget
from import_export.admin import ImportExportMixin
import logging


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("org_name", "short_org_name", "org_desc", "l_address", "bank_details", )
admin.site.register(Organization, OrganizationAdmin)


class UnitAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    mptt_indent_field = "unit_name"
    list_display = ('unit_name', 'unit_short_name', 'unit_cypher', )
admin.site.register(Unit, UnitAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ("position", )
admin.site.register(Position, PositionAdmin)


class PrefixAdmin(admin.ModelAdmin):
    list_display = ("prefix", )
admin.site.register(Prefix, PrefixAdmin)


class AreaCodeAdmin(admin.ModelAdmin):
    list_display = ("area_code", )
admin.site.register(AreaCode, AreaCodeAdmin)


class PostCodeAdmin(admin.ModelAdmin):
    list_display = ("post_code", )
admin.site.register(PostCode, PostCodeAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ("city", )
    filter_horizontal = ("area_code", )
admin.site.register(City, CityAdmin)


class StreetAdmin(admin.ModelAdmin):
    list_display = ("street", )
    filter_horizontal = ("post_code", )
admin.site.register(Street, StreetAdmin)


class BuildingAdmin(admin.ModelAdmin):
    list_display = ("building", )
admin.site.register(Building, BuildingAdmin)


class CampusAdmin(admin.ModelAdmin):
    list_display = ("campus", )
    filter_horizontal = ("prefix", )
admin.site.register(Campus, CampusAdmin)


class OfficeAdmin(admin.ModelAdmin):
    list_display = ("office", )
admin.site.register(Office, OfficeAdmin)


class WorkHoursAdmin(admin.ModelAdmin):
    list_display = ("begin_hours", "end_hours", )
admin.site.register(WorkHours, WorkHoursAdmin)


class PhoneForm(ModelForm):

    class Meta:
        widgets = {'number': EnclosedInput(prepend='внутр.'),}


class PhoneInline(SortableStackedInline):
    model = Phone
    extra = 1
    verbose_name_plural = 'Телефоны'


class PhoneAdmin(admin.ModelAdmin):
    form = PhoneForm
    list_display = ("country_code", "area_code", "prefix", "number", "is_outer",)
    list_editable = ("is_outer",)
admin.site.register(Phone, PhoneAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "building", "campus", "office", "city", )
admin.site.register(Address, AddressAdmin)


class DegreeAdmin(admin.ModelAdmin):
    suit_classes = 'suit-tab suit-tab-edu'
    list_display = ("degree", "short_degree", )
admin.site.register(Degree, DegreeAdmin)


class ScienceRankAdmin(admin.ModelAdmin):
    list_display = ("science_rank", "short_science_rank", )
admin.site.register(ScienceRank, ScienceRankAdmin)


class EduInline(SortableStackedInline, admin.TabularInline):
    model = Edu
    extra = 1
    max_num = 5
    suit_classes = 'suit-tab suit-tab-edu'


class EduAdmin(admin.ModelAdmin):
    list_display = ('level',)
admin.site.register(Edu, EduAdmin)

###################################
# django-select2 to model person  #
###################################


class PersonChoices(AutoModelSelect2Field):
    queryset = Person.objects
    search_fields = ['last_name__icontains', ]


class PositionChoices(AutoModelSelect2Field):
    queryset = Position.objects
    search_fields = ['position__icontains', ]


class UnitChoices(AutoModelSelect2Field):
    queryset = Unit.objects
    search_fields = ['unit_name__icontains', ]


# class AddressChoices(AutoModelSelect2Field):
#     queryset = Address.objects
#     search_fields = ['street', 'building', 'campus', 'office']

class PositionInUnitForm(ModelForm):
    position_verbose_name = Position._meta.verbose_name
    unit_verbose_name = Unit._meta.verbose_name
    person_verbose_name = Person._meta.verbose_name
    chief_verbose_name = PositionInUnit._meta.get_field('chief').verbose_name.title()
    address_verbose_name = Address._meta.verbose_name

    position = PositionChoices(
        label=position_verbose_name.capitalize(),
        requried=False,
        widget=AutoHeavySelect2Widget(
            select2_options={
                'width': '220px',
                'placeholder': 'Выберите %s ...' % position_verbose_name
            }
        )
    )
    unit = UnitChoices(
        label=unit_verbose_name.capitalize(),
        required=False,
        widget=AutoHeavySelect2Widget(
            select2_options={
                'width': '220px',
                'placeholder': 'Выберите %s ...' % unit_verbose_name
            }
        )
    )

    chief = PersonChoices(
        label=chief_verbose_name.capitalize(),
        required=False,
        widget=AutoHeavySelect2Widget(
            select2_options={
                'width': '220px',
                'placeholder': 'Выберите %s ...' % chief_verbose_name
            }
        )
    )

    # address = AddressChoices(
    #     label=address_verbose_name.capitalize(),
    #     required=False,
    #     widget=AutoHeavySelect2Widget(
    #         select2_options={
    #             'width': '220px',
    #             'placeholder': 'Выберите %s ...' % address_verbose_name
    #         }
    #     )
    # )

    class Meta:
        model = PositionInUnit
        fields = ['person', 'is_main', 'unit', 'position', 'phone', 'address', 'chief', ]


class PersonResource(resources.ModelResource):

    class Meta:
        model = Person


class PositionInUnitInline(SortableStackedInline, admin.TabularInline):
    model = PositionInUnit
    extra = 1
    max_num = 3
    verbose_name_plural = 'Должности'
    fk_name = 'person'
    suit_classes = 'suit-tab suit-tab-positioninunit'
    form = PositionInUnitForm
    filter_horizontal = ("phone", )

class PositionInUnitAdmin(admin.ModelAdmin):
    form = PositionInUnitForm
    filter_horizontal = ("phone", )
admin.site.register(PositionInUnit, PositionInUnitAdmin)


class PersonAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "email", "publish_date", "publish", )
    list_editable = ("publish",)
    # list_filter = ("unit",)
    # filter_horizontal = ("unit", "position", "phone", "address",)
    search_fields = ("last_name",)
    resource_class = PersonResource
    inlines = (EduInline, PositionInUnitInline)

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['user', 'publish', 'last_name', 'first_name', 'middle_name', 'birthday', 'email', 'photo']
        }),
        ('Звания/степени', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['degree', 'science_rank']
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-positioninunit',),
            'fields': ['work_hours',]
        }),

    ]

    suit_form_tabs = (('general', 'Основное'), ('positioninunit', 'Подразделение/Должность'), ('edu', 'Образование'), ('old','Должности/подразделения(старое)'),)

admin.site.register(Person, PersonAdmin)
########################################
#  end django-select2 to model person  #
########################################
