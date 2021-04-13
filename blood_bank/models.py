from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.template.loader import render_to_string

BloodGroup_Choices = (
    ('A+','A+'),
    ('A-', 'A-'),
    ('B+','B+'),
    ('B-', 'B-'),
    ('O+','O+'),
    ('O-', 'O-'),
    ('AB+','AB+'),
    ('AB-', 'AB-'),
)


# Create your models here.
class Bloodbank(models.Model):
    name = models.CharField(max_length=50)
    operator_email = models.EmailField(max_length=50)
    operator_password = models.CharField(max_length=254)
    date_created = models.DateTimeField(default =timezone.now)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    blood_bank = models.ForeignKey(Bloodbank, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=3, choices=BloodGroup_Choices, blank=True, null=True)
    donor_name = models.CharField(max_length=50)
    donor_address = models.CharField(max_length=254)
    mobile_no_pattern= RegexValidator(regex="^[0-9]{10}$", message="Entered mobile number isn't in a right format!")
    donor_mobile_no  = models.CharField(validators=[mobile_no_pattern], max_length=10, blank=True, null = True)
    donation_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, help_text="YYYY/MM/DD - eg: 1998-02-27")
    expiry_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, help_text="YYYY/MM/DD - eg: 1998-02-27")

    def __str__(self):
        return self.donor_name

class Transaction(models.Model):
    buyer_name = models.CharField(max_length=50)
    buyer_address = models.CharField(max_length=254)
    mobile_no_pattern= RegexValidator(regex="^[0-9]{10}$", message="Entered mobile number isn't in a right format!")
    buyer_mobile_no  = models.CharField(validators=[mobile_no_pattern], max_length=10, blank=True, null = True)
    donor_name = models.CharField(max_length=50)
    donor_address = models.CharField(max_length=254)
    donor_mobile_no  = models.CharField(validators=[mobile_no_pattern], max_length=10, blank=True, null = True)
    donation_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, help_text="YYYY/MM/DD - eg: 1998-02-27")
    selling_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, help_text="YYYY/MM/DD - eg: 1998-02-27")

    def __str__(self):
        return self.buyer_name