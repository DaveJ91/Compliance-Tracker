from django.urls import path

from . import views

urlpatterns = [
    path('declarations/', views.declaration_list, name='declaration_list')
]