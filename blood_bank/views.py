from django.shortcuts import render, redirect
from django.contrib import messages

# Models
from .models import *

# Forms
from main.forms import LoginForm
from .forms import  AddBloodForm

#decorators

def login__required(f):
    def wrap(request, *args, **kwargs):
        #this check the session if userid key exist, if not it will redirect to login page
        if 'operator_email' not in request.session.keys():
            messages.error(request, 'You are not logged in :/')
            return redirect("/operator/login")
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap


def is_operator(f):
    def wrap(request, *args, **kwargs):
        #this check the session if userid key exist, if not it will redirect to login page
        if 'is_operator' not in request.session.keys():
            messages.error(request, 'You are not an operator :/')
            return redirect("/dashboard")
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap


# Create your views here.

def login__as__operator(request):
    form = LoginForm()

    if request.method == "POST":
            form = LoginForm(request.POST)

            if form.is_valid():
                #Form Data
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                
                #User Object from database
                operator_obj = Bloodbank.objects.filter(operator_email=email).first()

                #Check If User Exists
                if operator_obj is None:
                    messages.error(request, 'User not found.')
                    return redirect('/operator/login')

                
                if operator_obj:
                        
                    #Check Password
                    is_valid_user = True if(password == operator_obj.operator_password) else False

                    #Case: Invalid Password
                    if not is_valid_user:
                        messages.error(request, 'Wrong password!')
                        return redirect('/operator/login')
                    else:                  
                        set_session(request, operator_obj.id, operator_obj.name, operator_obj.operator_email, 'true')
                        return redirect('/inventory')

    return render(request, 'main/log__in.html', {'form' : form})



# View Inventory
@login__required
@is_operator
def view__inventory(request):
    bloodbank_id = request.session['bloodbank_id']
    inventory = Inventory.objects.filter(blood_bank_id = bloodbank_id)
    return render(request, 'main/view_inventory.html', {'inventory' : inventory})


# Add Blood
@login__required
@is_operator
def add__blood(request):
    form = AddBloodForm()

    if request.method == 'POST':
        form = AddBloodForm(request.POST)

        if form.is_valid():
            blood_group = form.cleaned_data.get('blood_group')
            donor_name = form.cleaned_data.get('donor_name')
            donor_mobile_no = form.cleaned_data.get('donor_mobile_no')
            donation_date = form.cleaned_data.get('donation_date')

            

            #Bloodbank Obj
            bloodbank_id = request.session['bloodbank_id']
            blood_bank = Bloodbank.objects.filter(pk = bloodbank_id).first()

            #Blood Obj
            new_blood = Inventory.objects.create(blood_bank = blood_bank, blood_group = blood_group, donor_name = donor_name, donor_mobile_no = donor_mobile_no, donation_date = donation_date,)
            new_blood.save()
            print(new_blood.donation_date)
            messages.success(request, 'Blood Added Successfully')
            return redirect('/inventory')

    return render(request, 'main/add_blood.html', {'form' : form})



#Edit Blood

@login__required
@is_operator
def edit__blood(request,blood_id):

    blood_obj = Inventory.objects.get(pk=blood_id)

    form = AddBloodForm(request.POST or None, instance = blood_obj)

    if request.method == "POST":
        if form.is_valid():
            blood_group = form.cleaned_data.get('blood_group')
            donor_name = form.cleaned_data.get('donor_name')
            donor_mobile_no = form.cleaned_data.get('donor_mobile_no')
            donation_date = form.cleaned_data.get('donation_date')

            blood_obj.blood_group = blood_group
            blood_obj.donor_name = donor_name
            blood_obj.donor_mobile_no = donor_mobile_no
            blood_obj.donation_date = donation_date
            blood_obj.save()

            messages.success(request, 'Blood Details has been updated!') 
            return redirect('/inventory')

    else:
        return render(request, 'main/add_blood.html', {'form' : form}) 


#Delete Blood
@login__required
@is_operator
def delete__blood(request,blood_id):
    blood_obj = Inventory.objects.get(pk=blood_id)


    messages.success(request, 'Blood Deleted Succesfully!')
    blood_obj.delete()

    return render(request, 'main/delete_blood.html')
    



# Functions

def set_session(request, bloodbank_id, bloodbank_name, operator_email, is_operator):
    request.session['bloodbank_id'] = bloodbank_id
    request.session['bloodbank_name'] = bloodbank_name
    request.session['operator_email'] = operator_email
    request.session['is_operator'] = is_operator