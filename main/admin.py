from django.contrib import admin
from .models import *
from django.http import HttpResponse
from datetime import date
import csv


def generate_user_report(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename=User Report ' + \
        str(date.today())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Password',
                     'Authentication Token', 'Date Created'])

    users = queryset
    for user in users:
        writer.writerow([user.user_name, user.email,
                         user.password, user.auth_token, user.date_created])

    return response


def generate_donor_report(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename=Donor Report ' + \
        str(date.today())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Donor Name', 'Blood Group', 'Gender',
                     'Address', 'Mobile No', 'Date Created'])

    donors = queryset
    for donor in donors:
        writer.writerow([donor.user.user_name, donor.blood_group,
                         donor.gender, donor.city, donor.mobile_no, donor.date_created])

    return response


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'date_created')
    list_filter = ('date_created',)
    actions = [generate_user_report]


class DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'mobile_no', 'date_created')
    list_filter = ('date_created', 'blood_group',)
    actions = [generate_donor_report]


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.site_header = 'BloodBank Management System'
