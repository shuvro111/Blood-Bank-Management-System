from django.contrib import admin
from .models import *

class  UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'date_created')
    list_filter = ('date_created',)

class  DonorAdmin(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'mobile_no', 'date_created')
    list_filter = ('date_created', 'blood_group',)

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.site_header = 'BloodBank Management System'