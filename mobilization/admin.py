from django.contrib import admin
from .models import Person, FamilyMember, Index, City, Street, Protocol, Needs




admin.site.register(Person)
admin.site.register(FamilyMember)
admin.site.register(Index)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Protocol)
admin.site.register(Needs)
# Register your models here.
