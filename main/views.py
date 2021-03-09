from django.shortcuts import render, redirect
from django.contrib import messages
import uuid
from .models import *

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Send Mail
from django.conf import settings
from django.core.mail import send_mail

# Forms
from .forms import UserForm, LoginForm

#Hashing & Salting
from passlib.hash import pbkdf2_sha256

# Views


def index(request):
    return render(request, 'main/index.html')


def create__account(request):

    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            email = form.cleaned_data.get('email')

            password = form.cleaned_data.get('password')
            hashed_password = pbkdf2_sha256.hash(
                password, rounds=12000, salt_size=32)

            city = form.cleaned_data.get('city')
            mobile_no = form.cleaned_data.get('mobile_no')
            blood_group = form.cleaned_data.get('blood_group')
            gender = form.cleaned_data.get('gender')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            nid_image = form.cleaned_data.get('nid_image')
            is_donor = form.cleaned_data.get('is_donor')

            auth_token = str(uuid.uuid4())

            if User.objects.filter(email=email).first():
                messages.error(request, 'This email is already registered')
                return redirect('/token')
            else:
                new__user = User.objects.create(user_name=user_name, email=email, password=hashed_password, city=city, mobile_no=mobile_no, blood_group=blood_group, gender=gender, date_of_birth=date_of_birth, nid_image=nid_image, is_donor=is_donor, auth_token=auth_token)
                new__user.save()
                registration_mail(email, auth_token)
                return redirect('/token')
        else:
            return redirect('/create')
    else:
        return render(request, 'main/create__account.html', {'form': form})


def log__in(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            #Form Data
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            #User Object from database
            user_obj = User.objects.filter(email=email).first()

            #Check If User Exists
            if user_obj is None:
                messages.error(request, 'User not found.')
                return redirect('/login')

            #Check Verified User
            if not user_obj.is_verified:
                messages.error(request, 'Profile is not verified check your mail.')
                return redirect('/login')

            #Check Password
            hashed_password = user_obj.password
            is_valid_user = pbkdf2_sha256.verify(password, hashed_password)

            #Case: Invalid Password
            if not is_valid_user:
                messages.error(request, 'Wrong password!')
                return redirect('/login')
            
            #set_session / authorized login
            set_session(request, user_obj.user_name, user_obj.email)
            # if request.GET.get('next', None):
            #     return HttpResponseRedirect(request.GET['next'])
            # return HttpResponseRedirect(reverse('dashboard'))

            return redirect('/dashboard')

    return render(request, 'main/log__in.html', {'form' : form})


# @login_required(login_url='/login')
def log__out(request):
    request.session.flush()
    return redirect('/')

def token__send(request):
    return render(request, 'main/token.html')


def success(request):
    return render(request, 'main/success.html')

def error_page(request):
    return render(request, 'main/error.html')
# @login_required(login_url='/login')
def dashboard(request):
    return render(request, 'main/dashboard.html')


# Functions

def registration_mail(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link http://127.0.0.1:8000/verify/{token} or click on the link to verify your account'


    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def verify(request , auth_token):
    try:
        user_obj = User.objects.filter(auth_token = auth_token).first()
    

        if user_obj:
            if user_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            user_obj.is_verified = True
            user_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')


def set_session(request, username, email):
    request.session['username'] = username
    request.session['email'] = email