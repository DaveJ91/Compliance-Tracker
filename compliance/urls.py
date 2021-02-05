from django.urls import path

from . import views

urlpatterns = [
    path('declarations/', views.declaration_list, name='declaration_list'),
    path('declarations/<id>/', views.declaration_detail, name='declaration_detail')
]