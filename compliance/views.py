from django.shortcuts import render
from django.template import loader

from .models import *

# List Views
def declaration_list(request):
    declarations = Declaration.objects.all()
    context = {'declaration_list':declaration_list}
    return render(request, 'compliance/list/declaration_list.html', context)

def team_member_list(request):
    team_members = TeamMember.objects.all()
    context = {'team_members': team_members}
    return render(request, 'compliance/list/team_member_list.html', context)

def country_list(request):
    countries = Country.objects.all()
    context = {'countries': countries}
    return render(request, 'compliance/list/country_list.html',context)

def tax_registration_list(request):
    tax_registrations = TaxRegistration.objects.all()
    context = TaxRegistration.objects.all()
    return render(request, 'compliance/list/tax_registration_list.html',context)

def division_list(request):
    divisions = Division.objects.all()
    context = {'divisions', divisions}
    return render(request, 'compliance/divisions/division_list.hmtl')

# Detail Views
def declaration_detail(request,id):
    declaration = Declaration.objects.get(pk=id)
    context = {'declaration': declaration}
    return render(request, 'compliance/detail/declaration_detail.html', context)

def team_member_detail(request, id):
    team_member = TeamMember.objects.get(pk=id)
    context = {'team_member':team_member}
    return render(request, 'compliance/detil/team_member_detail.html', context)

def country_detail(request, id):
    country = Country.objects.get(pk=id)
    context = {'country': country}
    return render(request, 'compliance/detail/country_detail.html', context)

def tax_registration_detail(request, id):
    tax_registration = TaxRegistration.objects.get(pk=id)
    context = {'tax_registration': tax_registration}
    return render(request, 'compliance/detail/tax_registration_detail.html')

def division_detail(request, id):
    division = Division.objects.get(pk=id)
    context = {'division': division}
    return render(request, 'compliance/detail/division_detail.html')


    

