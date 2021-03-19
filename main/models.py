from django.db import models

# Create your models here.
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

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
Gender_Choices = (
    ('Male','Male'),
    ('Female','Female'),
)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=254)
    is_verified = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=100)
    date_created = models.DateTimeField(default =timezone.now)

    def __str__(self):
        return self.user_name

class Donor(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    mobile_no_pattern= RegexValidator(regex="^[0-9]{10}$", message="Entered mobile number isn't in a right format!")
    mobile_no  = models.CharField(validators=[mobile_no_pattern], max_length=10, blank=True, null = True)
    blood_group = models.CharField(max_length=3, choices=BloodGroup_Choices, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=Gender_Choices, blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True, help_text="YYYY/MM/DD - eg: 1998/02/27")
    nid_image = models.FileField(upload_to='static/assets/nid/%Y/%m/%d/', max_length=100, blank=True, null=True)
    is_donor = models.BooleanField(default=False, blank=True)


    def __str__(self):
        return self.user.user_name

    





# class  Bookmark(models.Model):
#     donor = models.OneToOneField("Donor", on_delete=models.CASCADE)
#     user = models.ManyToManyField("User")