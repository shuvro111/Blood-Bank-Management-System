from django import forms
from django.core.validators import *
from .models import *

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

class DateInput(forms.DateInput):
    input_type = 'date'




class UserForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    password = forms.CharField(label='Password', max_length=254, widget=forms.PasswordInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))

    is_donor = forms.BooleanField(label='Register as donor', initial=True, required = False, widget=forms.CheckboxInput())

    city = forms.CharField(required = False, label='City', max_length=50, widget=forms.TextInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    mobile_no = forms.CharField(required = False, label='Mobile No', widget=forms.TextInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'onkeyup': 'validate_mobile_no()', 'minlength' : '10', 'maxlength' : '10', 'required':''}))
    blood_group = forms.ChoiceField(required = False, label='Blood Group', choices = BloodGroup_Choices, widget=forms.Select(attrs = {'class':"w-full text-sm py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    gender = forms.ChoiceField(required = False, label='Gender', choices = Gender_Choices, widget=forms.Select(attrs = {'class':"w-full text-sm py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    date_of_birth = forms.DateField(required = False, widget = DateInput(attrs={'class':'text-sm py-2 border-b border-gray-300 focus:outline-none focus:border-red-500','value':'1990-01-01', 'required':''}))
    nid_image = forms.ImageField(required = False,  widget=forms.FileInput(attrs={'required':''}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''}))
    password = forms.CharField(label='Password', max_length=254, widget=forms.PasswordInput(attrs = {'class':"w-full text-md py-1 border-b border-gray-300 focus:outline-none focus:border-red-500", 'required':''})) 


