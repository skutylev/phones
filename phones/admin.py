from django.contrib import admin
from phones.models import Organization, Unit, Position, Prefix, AreaCode, PostCode, City, Street, Building, Campus, Office, Phone, Address, Person, Degree, ScienceRank
from django_mptt_admin.admin import DjangoMpttAdmin


class UnitAdmin(DjangoMpttAdmin):
    pass

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "address")
    list_filter = ("last_name",)
    filter_horizontal = ("unit", "position", "phone",)
    search_fields = ("last_name", "unit", "position", "phone",)

admin.site.register(Organization)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Position)
admin.site.register(Prefix)
admin.site.register(AreaCode)
admin.site.register(PostCode)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Building)
admin.site.register(Campus)
admin.site.register(Office)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Degree)
admin.site.register(ScienceRank)
admin.site.register(Person, PersonAdmin)
