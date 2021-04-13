from django.contrib import admin
from  .models import  *

class  BloodbankAdmin(admin.ModelAdmin):
    list_display = ('name', 'operator_email', 'operator_password')

class  InventoryAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'donor_address', 'blood_group', 'donation_date', 'blood_bank')

class  TransactionAdmin(admin.ModelAdmin):
    list_display = ('buyer_name', 'buyer_address', 'buyer_mobile_no','donor_name', 'donor_address', 'donor_mobile_no', 'selling_date')

# Register your models here.
admin.site.register(Bloodbank, BloodbankAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Transaction, TransactionAdmin)