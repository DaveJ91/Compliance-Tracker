from django.shortcuts import render
from django.template import loader

from .models import *

def declaration_index(request):
    declaration_list = Declaration.objects.all()
    context = {'declaration_list':declaration_list}
    return render(request, 'compliance/declaration_list.html', context)