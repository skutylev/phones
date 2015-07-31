from django.contrib import admin
from phones.models import Organization, Unit, Position, Prefix, AreaCode, PostCode, City, Street, Building, Campus, Office, Phone, Address, Person

# Register your models here.

class PostCodeInline(admin.StackedInline):
    model = PostCode
    extra = 3

class StreetAdmin(admin.ModelAdmin):
    inlines = [PostCodeInline]

admin.site.register(Organization)
admin.site.register(Unit)
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
admin.site.register(Person)


