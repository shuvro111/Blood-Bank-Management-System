from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views


urlpatterns = [
    path('operator/login', views.login__as__operator, name = 'login__as__operator'),
    path('inventory/pages=<int:page_number>', views.view__inventory, name = 'view__inventory'),
    path('inventory/add/', views.add__blood, name = 'add__blood'),
    path('inventory/edit/<int:blood_id>', views.edit__blood, name = 'edit__blood'),
    path('inventory/delete/<int:blood_id>', views.delete__blood, name = 'delete__blood'),
]




