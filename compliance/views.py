from django.shortcuts import render
from django.template import loader

from .models import *

# List Views
def declaration_list(request):
    declaration_list = Declaration.objects.all()
    context = {'declaration_list':declaration_list}
    return render(request, 'compliance/list/declaration_list.html', context)

def team_member_list(request):
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'compliance/list/team_member_list.html', context)

def country_list(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'compliance/list/country_list.html')

def tax_registration_list(request):
    tax_registrations = TaxRegistration.objects.all()
    context = TaxRegistration.objects.all()
    return render(request, 'compliance/list/tax_registration_list.html')

