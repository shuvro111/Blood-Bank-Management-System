from django import forms

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


class UserForm(forms.Form):
    user_name = forms.CharField(label='Name', max_length=50)
    email = forms.forms.EmailField(label='Email', max_length=254)
    password = forms.(label='Password', widget=forms.PasswordInput, max_length=254)

    is_donor = forms.BooleanField(label='Register as donor', max_length=50)

    city = forms.CharField(label='City', max_length=50)
    mobile_no = forms.IntegerField(label='Mobile No', max_length=10)
    blood_group = forms.ChoiceField(label='Blood Group', choices = BloodGroup_Choices)
    gender = forms.ChoiceField(label='Gender', choices = Gender_Choices)
    date_of_birth = forms.DateField(label='Date Of Birth')
    nid_image = forms.ImageField(label='Upload your NID image')

