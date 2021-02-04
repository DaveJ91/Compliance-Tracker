from django.contrib import admin

# Register your models here.
from .models import Division, Country, TeamMember, Tax_Registration, Declaration

admin.site.register(Division)
admin.site.register(Country)
admin.site.register(TeamMember)
admin.site.register(Tax_Registration)
admin.site.register(Declaration)
