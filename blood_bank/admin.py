from django.contrib import admin
from  .models import  *
from django.http import HttpResponse
from datetime import date
import csv

def generate_bloodbank_report(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename=Bloodbank Report '+str(date.today())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Bloodbank Name', 'Operator Email', 'Operator Password','Date Created'])

    bloodbanks = queryset
    for bloodbank in bloodbanks:
        writer.writerow([bloodbank.name, bloodbank.operator_email, bloodbank.operator_password, bloodbank.date_created])
    
    return response

def generate_inventory_report(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename=Inventory Report '+str(date.today())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Bloodbank Name', 'Blood Group', 'Donor Name', 'Donor Address','Donor Mobile No', 'Donation Date', 'Expiry Date'])

    inventories = queryset
    for inventory in inventories:
        writer.writerow([inventory.blood_bank.name, inventory.blood_group, inventory.donor_name, inventory.donor_address, inventory.donor_mobile_no, inventory.donation_date, inventory.expiry_date])
    
    return response

def generate_transaction_report(modeladmin,request,queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename=Transaction Report '+str(date.today())+'.csv'
    writer = csv.writer(response)
    writer.writerow(['Blood Group', 'Buyer Name', 'Buyer Address', 'Buyer Mobile No', 'Donor Name', 'Donor Address', 'Donor Mobile No', 'Donation Date', 'Selling Date'])

    transactions = queryset
    for transaction in transactions:
        writer.writerow([transaction.blood_group, transaction.buyer_name, transaction.buyer_address, transaction.buyer_mobile_no, transaction.donor_name, transaction.donor_address, transaction.donor_mobile_no, transaction.donation_date, transaction.selling_date])
    
    return response




class  BloodbankAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator_email', 'operator_password')
    actions = [generate_bloodbank_report]

class  InventoryAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'donor_address', 'blood_group', 'donation_date', 'blood_bank')
    actions = [generate_inventory_report]

class  TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'buyer_address', 'buyer_mobile_no','donor_name', 'donor_address', 'donor_mobile_no', 'selling_date')
    actions = [generate_transaction_report]

# Register your models here.
admin.site.register(Bloodbank, BloodbankAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Transaction, TransactionAdmin)