from django.urls import path,include

from . import views

urlpatterns = [
    path('declarations/', views.declaration_list, name='declaration_list'),
    path('declarations/<id>/', views.declaration_detail, name='declaration_detail'),
    path('login/', views.user_login_view, name='user_login'),
    path('logout/', views.user_logout_view, name='user_logout')
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]