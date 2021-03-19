from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404
import uuid

# Send Mail
from django.conf import settings
from django.core.mail import send_mail

#Hashing & Salting
from passlib.hash import pbkdf2_sha256

#Models
from .models import *
from bookmark.models import *

# Forms
from .forms import UserForm, LoginForm, UserUpdateForm, DonorUpdateForm



# Decorators

def login__required(f):
    def wrap(request, *args, **kwargs):
        #this check the session if userid key exist, if not it will redirect to login page
        if 'email' not in request.session.keys():
            messages.error(request, 'You are not logged in :/')
            return redirect("/login")
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap





# Views


def index(request):
    if 'email' not in request.session.keys():
        return render(request, 'main/index.html')
    else:
        return redirect('dashboard')



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

            print("is donor is", is_donor)

            auth_token = str(uuid.uuid4())

            #Check if account exists
            user_obj = User.objects.filter(email=email).first()

            if user_obj:
                messages.error(request, 'This email is already registered')
                return redirect('/token')
            else:
                new__user = User.objects.create(user_name=user_name, email=email, password=hashed_password, auth_token=auth_token)

                if is_donor:
                    new__donor = Donor.objects.create(is_donor = is_donor, user = new__user, city=city, mobile_no=mobile_no, blood_group=blood_group, gender=gender, date_of_birth=date_of_birth, nid_image=nid_image)
                    new__donor.save()
                else:
                    new__user.save()
   
                registration_mail(email, auth_token)
                return redirect('/token')
        else:
            return redirect('/create')
    else:
        return render(request, 'main/create__account.html', {'form': form})


def log__in(request):

    if 'email' in request.session.keys():
        return redirect('/dashboard')

    else:
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

                
                if user_obj:

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
                    else:                  
                        #check if donor or user
                        is_donor = hasattr(user_obj, 'donor')

                        if is_donor:
                            #set_session / authorized login
                            set_session(request, user_obj.id, user_obj.user_name, user_obj.email, 'true')
                        else:
                            #set_session / authorized login
                            set_session(request, user_obj.id, user_obj.user_name, user_obj.email, 'false')

                        return redirect('/dashboard')


                

        return render(request, 'main/log__in.html', {'form' : form})


@login__required
def log__out(request):
    request.session.flush()
    return redirect('/')


@login__required
def edit__profile(request):
    
    id = request.session['user_id']
    # user_obj = get_object_or_404(User, pk=id)
    user_obj = User.objects.get(pk=id)
    is_donor = hasattr(user_obj, 'donor')

    form = UserUpdateForm(request.POST or None, instance = user_obj)
    if is_donor:
        donor_obj = Donor.objects.filter(user = user_obj).first()
        print(donor_obj.user_id)
        donor_form = DonorUpdateForm(request.POST or None, instance = donor_obj)

    if request.method == "POST":
        

        if form.is_valid():
            print("Form is valid")
            user_name = form.cleaned_data.get('user_name')
            user_obj.user_name = user_name
            user_obj.save()

    if request.method == "POST":
        print("POST METHOD Received")
        if is_donor:
            print(donor_form.errors)
            if donor_form.is_valid():

                
                city = donor_form.cleaned_data.get('city')
                mobile_no = donor_form.cleaned_data.get('mobile_no')
                gender = donor_form.cleaned_data.get('gender')
                date_of_birth = donor_form.cleaned_data.get('date_of_birth')

                # donor_obj.user = user_obj
                print(city)
                donor_obj.city = city
                donor_obj.mobile_no = mobile_no
                donor_obj.gender = gender
                donor_obj.date_of_birth = date_of_birth
                
                donor_obj.save()
                print('donor object saved')
        
        messages.success(request, 'Profile has been updated!') 
        return redirect('/dashboard')

    else:
        if is_donor:
            return render(request, 'main/edit_profile.html', {'form' : form, 'donor_form' : donor_form})
        else:
            return render(request, 'main/edit_profile.html', {'form' : form})        

    
@login__required
def view__donors(request):
    donors = Donor.objects.all()
    
    id = request.session['user_id']
    user_obj = User.objects.get(pk=id)
    bookmarks = Bookmark.objects.filter(client = user_obj)

    # donor_id = request.POST['donor_id']
    # donor_obj = Donor.objects.get(pk=donor_id)

    return render(request, 'main/view_donors.html', {'donors' : donors, 'bookmarks' : bookmarks, 'bookmarked' : 'False'})


def token__send(request):
    return render(request, 'main/token.html')


def success(request):
    return render(request, 'main/success.html')

def error_page(request):
    return render(request, 'main/error.html')

@login__required
def dashboard(request):
    if request.session['is_donor'] == 'true':
        return render(request, 'main/donor_dashboard.html')
    else:
        return render(request, 'main/user_dashboard.html')

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


def set_session(request, user_id, user_name, email, donor_status):
    request.session['user_id'] = user_id
    request.session['user_name'] = user_name
    request.session['email'] = email
    request.session['is_donor'] = donor_status

