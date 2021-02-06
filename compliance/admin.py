from django.contrib import admin

# Register your models here.
from .models import Division, Country, TaxRegistration, Declaration

admin.site.register(Division)
admin.site.register(Country)
admin.site.register(TaxRegistration)
admin.site.register(Declaration)
