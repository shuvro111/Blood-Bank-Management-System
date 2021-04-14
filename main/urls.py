from django.contrib import admin
from django.urls import path, include

from . import views
from . import admin

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create__account, name = 'create__account'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error"),
    path('login/', views.log__in, name = 'log__in'),
    path('logout/', views.log__out, name = 'log__out'),
    path('user/profile/edit/', views.edit__profile, name = 'edit__profile'),
    path('token/', views.token__send, name = 'token__send'),
    path('success/', views.success, name = 'success'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('donors/', views.view__donors, name = 'view__donors'),
    path('sort_by_nearest/', views.sort_by_nearest, name = 'sort_by_nearest'),
    path('generate_user_report/', admin.generate_user_report, name = 'generate_user_report'),
    path('generate_donor_report/', admin.generate_donor_report, name = 'generate_donor_report'),
]
