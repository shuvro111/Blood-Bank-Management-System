from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create__account, name = 'create__account'),
    path('login/', views.log__in, name = 'log__in'),
    path('admin/', admin.site.urls),
]
