from django.contrib import admin
from phones.models import Organization, Unit, Position, Prefix, AreaCode, PostCode, City, Street, Building, Campus, Office, WorkHours, Phone, Address, Person, Degree, ScienceRank
from django_mptt_admin.admin import DjangoMpttAdmin

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("org_name", "short_org_name", "org_desc", "l_address", "bank_details", )

class UnitAdmin(DjangoMpttAdmin):
    pass

class PositionAdmin(admin.ModelAdmin):
    list_display = ("position", "chief_position", "subordinate_position", )

class PrefixAdmin(admin.ModelAdmin):
    list_display = ("prefix", )

class AreaCodeAdmin(admin.ModelAdmin):
    list_display = ("area_code", )

class PostCodeAdmin(admin.ModelAdmin):
    list_display = ("post_code", )

class CityAdmin(admin.ModelAdmin):
    list_display = ("city", )
    filter_horizontal = ("area_code", )

class StreetAdmin(admin.ModelAdmin):
    list_display = ("street", )
    filter_horizontal = ("post_code", )

class BuildingAdmin(admin.ModelAdmin):
    list_display = ("building", )

class CampusAdmin(admin.ModelAdmin):
    list_display = ("campus", )
    filter_horizontal = ("prefix", )

class OfficeAdmin(admin.ModelAdmin):
    list_display = ("office", )

class WorkHoursAdmin(admin.ModelAdmin):
    list_display = ("schedule", "begin_hours", "end_hours", )

class PhoneAdmin(admin.ModelAdmin):
    list_display = ("country_code", "area_code", "prefix", "number", )

class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "building", "campus", "office", )

class DegreeAdmin(admin.ModelAdmin):
    list_display = ("degree", "short_degree", )

class ScienceRankAdmin(admin.ModelAdmin):
    list_display = ("science_rank", "short_science_rank", )

class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "address", "email", "photo", "publish_date", "publish", )
    list_editable = ("publish", )
    list_filter = ("last_name",)
    filter_horizontal = ("unit", "position", "phone",)
    search_fields = ("last_name", "unit", "position", "phone",)

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Prefix, PrefixAdmin)
admin.site.register(AreaCode, AreaCodeAdmin)
admin.site.register(PostCode, PostCodeAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Campus, CampusAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(WorkHours, WorkHoursAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(ScienceRank, ScienceRankAdmin)
admin.site.register(Person, PersonAdmin)

