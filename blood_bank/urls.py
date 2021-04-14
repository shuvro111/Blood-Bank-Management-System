from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views
from . import admin


urlpatterns = [
    path('operator/login', views.login__as__operator, name = 'login__as__operator'),
    path('inventory/', views.view__inventory, name = 'view__inventory'),
    path('inventory/add/', views.add__blood, name = 'add__blood'),
    path('inventory/edit/<int:blood_id>', views.edit__blood, name = 'edit__blood'),
    path('inventory/delete/<int:blood_id>', views.delete__blood, name = 'delete__blood'),
    path('inventory/confirm-sell/<int:blood_id>', views.sell__blood, name = 'sell__blood'),
    path('inventory/expirydetails', views.expiry__details, name = 'expiry__details'),
    
    path('generate_bloodbank_report/', admin.generate_bloodbank_report, name = 'generate_bloodbank_report'),
    path('generate_inventory_report/', admin.generate_bloodbank_report, name = 'generate_inventory_report'),
    path('generate_transaction_report/', admin.generate_bloodbank_report, name = 'generate_transaction_report'),
]




