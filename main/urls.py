from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create__account, name = 'create__account'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error"),
    path('login/', views.log__in, name = 'log__in'),
    path('logout/', views.log__out, name = 'log__out'),
    path('token/', views.token__send, name = 'token__send'),
    path('success/', views.success, name = 'success'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
]
