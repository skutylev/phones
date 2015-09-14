from django.contrib import admin
from phones.models import Organization, Unit, Position, Prefix, AreaCode, PostCode, City, Street, Building, Campus, Office, WorkHours, Phone, Address, Person, Degree, ScienceRank, Edu
from django.forms import ModelForm
from suit.widgets import EnclosedInput
from mptt.admin import MPTTModelAdmin

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("org_name", "short_org_name", "org_desc", "l_address", "bank_details", )
admin.site.register(Organization, OrganizationAdmin)

class UnitAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    mptt_indent_field = "unit_name"
    list_display = ('unit_name', 'unit_cypher', )
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

class PhoneAdmin(admin.ModelAdmin):
    form = PhoneForm
    list_display = ("country_code", "area_code", "prefix", "number", )
admin.site.register(Phone, PhoneAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "building", "campus", "office", "city", )
admin.site.register(Address, AddressAdmin)

class DegreeAdmin(admin.ModelAdmin):
    list_display = ("degree", "short_degree", )
admin.site.register(Degree, DegreeAdmin)

class ScienceRankAdmin(admin.ModelAdmin):
    list_display = ("science_rank", "short_science_rank", )
admin.site.register(ScienceRank, ScienceRankAdmin)

class EduAdmin(admin.ModelAdmin):
    list_display = ('level',)
    model = Edu
    extra = 1
    max_num = 5
admin.site.register(Edu, EduAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "email", "get_phones", "publish_date", "publish" )
    list_editable = ("publish",)
    list_filter = ("unit", "chief")
    filter_horizontal = ("unit", "position", "phone", "address", )
    search_fields = ("last_name",)
admin.site.register(Person, PersonAdmin)
