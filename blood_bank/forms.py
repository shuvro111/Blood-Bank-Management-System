from django import forms
from django.forms import ModelForm
from django.core.validators import *
from .models import *

class AddBloodForm(forms.ModelForm):
    blood_group = forms.ChoiceField(required = False, label='Blood Group', choices = BloodGroup_Choices, widget=forms.Select(attrs = {'class':"w-full text-sm py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    donor_name = forms.CharField(required = False, label='Donor Name', max_length=50, widget=forms.TextInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    donor_mobile_no = forms.CharField(required = False, label="Donor's Mobile No", widget=forms.TextInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'onkeyup': 'validate_mobile_no()', 'minlength' : '10', 'maxlength' : '10', 'required':''}))
    donation_date = forms.DateField(required = False, widget = forms.DateInput(attrs={'type': 'date','class':'text-sm py-2 border-b border-gray-300 focus:outline-none focus:border-red-500', 'required':''}))
    class Meta:
        model = Inventory
        exclude = ['blood_bank']