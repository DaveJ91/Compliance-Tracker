from django.urls import path

from . import views

urlpatterns = [
    path('declarations/', views.declaration_index, name='declaration_list')
]