from django.contrib import admin
from .models import *
from django.http import HttpResponse
import csv,datetime

def generate_report(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename=Report'+str(datetime.datetime.now())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email', 'Password', 'Authentication Token', 'Date Created'])

    users = queryset
    for user in users:
        writer.writerow([user.user_name, user.email, user.password, user.auth_token, user.date_created])
    
    return response


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'date_created')
    list_filter = ('date_created',)
    actions = [generate_report]

class DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'mobile_no', 'date_created')
    list_filter = ('date_created', 'blood_group',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.site_header = 'BloodBank Management System'