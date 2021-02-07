from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Division, Country, TaxRegistration, Declaration

admin.site.register(Division)
admin.site.register(Country)
admin.site.register(TaxRegistration)
admin.site.register(Declaration)
