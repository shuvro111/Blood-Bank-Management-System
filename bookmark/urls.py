from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views


urlpatterns = [
    path('bookmarks/', views.view__bookmarks, name='view__bookmarks'),
    path('addbookmarks/<int:donor_id>',
         views.add__bookmarks, name='add__bookmarks'),
    path('removebookmarks/<int:donor_id>',
         views.remove__bookmarks, name='remove__bookmarks'),
    # url(r'^addbookmarks$', views.add__bookmarks, name='add__bookmarks'),
]
