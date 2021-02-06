from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout

from .models import *

# User Authentication Views
def user_login_view(request):
    print(request)

    if request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            print('logged in')
        else:
            # No backend authenticated the credentials
            print('invalid user')
        
    else:
        print('get')
    
    context={}
    return render(request, 'compliance/user_authentication/login.html', context)

def user_logout_view(request):
    logout(request)
    return redirect(user_login_view)


# List Views
def declaration_list(request):
    declarations = Declaration.objects.all()
    context = {'declarations':declarations}
    return render(request, 'compliance/list/declaration_list.html', context)


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




    

