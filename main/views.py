from django.shortcuts import render, redirect
from django.contrib import messages
import uuid
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from passlib.hash import pbkdf2_sha256

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def create__account(request):
    
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')

        password = request.POST.get('password')
        hashed_password = pbkdf2_sha256.hash(password, rounds = 12000, salt_size = 32)

        city = request.POST.get('city')
        blood_group = request.POST.get('blood_group')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        nid_image = request.POST.get('nid_image')
        
        is_donor_value = request.POST.get('is_donor_value')
        if(is_donor_value == "True"):
            is_donor = True
        else:
            is_donor = False

        print("Updated is donor")
        print(is_donor)
        


        auth_token = str(uuid.uuid4())


        if User.objects.filter(email = email).first():
            messages.error(request, 'This email is already registered')
            return redirect('/token')


        new__user = User.objects.create(user_name = user_name, email = email, password = hashed_password, city = city, blood_group = blood_group, gender = gender, date_of_birth = date_of_birth, nid_image = nid_image, is_donor = is_donor, auth_token = auth_token)
        new__user.save()


    return render(request, 'main/create__account.html') 
 
def log__in(request):
    return render(request, 'main/log__in.html') 

def token__send(request):
    return render(request, 'main/token.html') 

def success(request):
    return render(request, 'main/success.html') 

def dashboard(request):
    return render(request, 'main/dashboard.html') 

