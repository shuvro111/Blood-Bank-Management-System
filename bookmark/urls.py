from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views


urlpatterns = [
    path('bookmarks/', views.view__bookmarks, name = 'view__bookmarks'),
    path('addbookmarks/', views.add__bookmarks, name = 'add__bookmarks'),
    # url(r'^addbookmarks$', views.add__bookmarks, name='add__bookmarks'),
]




