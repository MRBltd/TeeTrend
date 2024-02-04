from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserAccountForm , EmailSignInForm , SignInOtpForm , deactivateOtpForm , EditProfileForm
from .models import UserAccount
from django.core.mail import send_mail
import random
import pyotp
import string
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db import IntegrityError
from django.utils import timezone
from datetime import timedelta
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


# The User entering details
def account(request):
  if 'user_id' in request.session:
    try:
      user_id = request.session['user_id']
      print(user_id)
      accts = UserAccount.objects.get(id=user_id)  
      return render(request, 'account_details.html', {'accts': accts})
    except UserAccount.DoesNotExist:
      return redirect('sign_in')
  else:
    return redirect('sign_in')      

def profileOverview(request):
  return render(request , 'account_details.html')

# Otp Generating function
def generate_otp(length=6):
  base32secret = pyotp.random_base32()
  otp = pyotp.TOTP(base32secret, interval=60, digits=6)
  print(otp)
  return otp.now()

# The User signup function
def sign_up(request):
  if request.method == 'POST':
    form = UserAccountForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data.get('email')
      # Check if the email already exist in the database
      if UserAccount.objects.filter(email=email).exists():
        form.add_error('email', 'This email is already in use')
        return render(request, 'sign_up.html', {'form': form})
      else:
        otp = generate_otp() # The Generated otp will saving in otp named variable
        print(otp)
        user = form.save(commit=False)
        user.otp = otp
        try:
          user.save() # The otp saving in the database
          jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
          jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
          payload = jwt_payload_handler(user)
          token = jwt_encode_handler(payload)
          print(token)
          response = redirect('verify_otp')
          response.set_cookie('user_id', user.id)  # sets a cookie
          response.set_cookie('jwt', token)  # sets the jwt token as a cookie
          return response
        except IntegrityError:
          form.add_error('email', 'An error occurred while saving the user')
          return render(request, 'sign_up.html', {'form': form})
        # The otp sending at user email
        send_mail(
          'Your OTP for Registration',
          f'Your OTP is: {otp}',
          'midhunbalachandran07@gmail.com',
          [email],
        )
        messages.success(request , f'Your User email is {email}')
        return redirect('verify_otp')
  else:
    form = UserAccountForm()
  return render(request, 'sign_up.html', {'form': form})

# The otp verification with email(the user enter the sign up email and otp for send the user email)
def verify_otp(request):
  if request.method == 'POST':
    form = SignInOtpForm(request.POST)
    if form.is_valid():
      otp = form.cleaned_data.get('otp')
      try:
        user = UserAccount.objects.get(otp=otp)
        if user.otp == otp:
          user.is_verified = True  
          user.save()  # save the change to the database
          request.session['user_id'] = user.id 
          messages.success(request, 'Logged in successfully')
          return redirect('home')
        else:
          form.add_error('otp', 'Invalid OTP.. Enter a correct OTP and click the sign in button')
      except ObjectDoesNotExist:
        form.add_error(None, 'Invalid OTP.. Enter a correct OTP and click the sign in button')
  else:
      form = SignInOtpForm()
  return render(request , 'verify_otp.html' , {'form' : form})

# The user signin function (using email)
def sign_in(request):
  user_id = request.COOKIES.get('user_id')
  if request.method == 'POST':
    form = EmailSignInForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data.get('email')
      user = UserAccount.objects.filter(email=email).first()
      if user:
        # Check the number of sign-ins in the last 24 hours
        # Check the number of sign-ins in the last 24 hours
        one_day_ago = timezone.now() - timedelta(days=1)
        recent_sign_ins = UserAccount.objects.filter(email=email, sign_in_timestamp__gte=one_day_ago).count()
        print(recent_sign_ins)
        if recent_sign_ins >= 5:
          print('Hello..')
          # Too many sign-ins
          form.add_error('email', 'Too many sign-ins in the last 24 hours.')
          return render(request, 'sign_in.html', {'form': form})
        otp = generate_otp() # The Generated otp will saving in otp named variable
        user.otp = otp
        try:
          user.save() # The otp saving in the database
        except IntegrityError:
          form.add_error('email', 'An error occurred while saving the user')
          return render(request, 'sign_in.html', {'form': form})
        # The otp sending at user email
        send_mail(
          'Your OTP',
          f'Your OTP is {otp}',
          'midhunbalachandran07@gmail.com' ,
          [user.email],
        )
        return redirect('sign_in_verify_otp')
      else:
        form.add_error('email', 'No user with this email exists')
  else:
    form = EmailSignInForm()
  return render(request, 'sign_in.html', {'form': form})


# The Otp verification 
def sign_in_verify_otp(request):
  if request.method == 'POST':
    form = SignInOtpForm(request.POST)
    if form.is_valid():
      otp = form.cleaned_data.get('otp')
      try:
        user = UserAccount.objects.get(otp=otp)
        if user.otp == otp:
          user.is_verified = True  
          user.save()  # save the change to the database
          request.session['user_id'] = user.id 
          messages.success(request, 'Logged in successfully')
          return redirect('home')
        else:
          form.add_error('otp', 'Invalid OTP.. Enter a correct OTP and click the sign in button')
      except ObjectDoesNotExist:
        form.add_error(None, 'Invalid OTP.. Enter a correct OTP and click the sign in button')
  else:
      form = SignInOtpForm()
  return render(request, 'verify_otp.html', {'form': form})

# The Profile edit function
def edit_profile(request):
  if 'user_id' not in request.session:
    return redirect('sign_in')  # Redirect to sign in page if user is not logged in
  user_id = request.session['user_id']
  user = UserAccount.objects.get(id=user_id)
  if request.method == 'POST':
    form = EditProfileForm(request.POST, instance=user)
    if form.is_valid():
      form.save()
      return redirect('account')  # Redirect to profile page after successful update
  else:
    form = EditProfileForm(instance=user)
  return render(request, 'edit_profile.html', {'form': form})

# The User logout function
def logout_view(request):
  request.session.pop('user_id', None)
  return redirect('sign_in')

# The function for  User complete the signup or signin the home page will make some changes
def profile(request):
  accts = None
  if 'user_id' in request.session:
    user_id = request.session['user_id']
    try:
      accts = UserAccount.objects.get(id=user_id)
    except UserAccount.DoesNotExist:
      print("UserAccount does not exist")
  return render(request, 'home.html', {'accts': accts})

def account_deactivation_warning(request):
  return render(request , 'account_deletion.html')

# @login_required
def deactivate_account(request):
  sign_in_url = reverse('sign_in')
  if request.method == 'POST':
    if 'user_id' in request.session:
      user_id = request.session['user_id']
      try:
        user = UserAccount.objects.get(id=user_id)  # Get the User instance
        # Generate an OTP
        otp = generate_otp()
        request.session['otp'] = otp
        # Send OTP to user's email
        send_mail(
          'Account Deactivation OTP',
          f'Your OTP for account deactivation is {otp}',
          'midhunbalachandran07@gmail.com',
          [user.email],
          fail_silently=False,
        )
        form = deactivateOtpForm()
        return render(request , 'delete_account_confirm.html', {'form': form, 'email': user.email})
      except UserAccount.DoesNotExist:
        print(f"No UserAccount found for id {user_id}")
    else:
      return HttpResponse(f'''
      <h3>No user account. Sign in to your account...</h3>
      <a href="{sign_in_url}" style="color: white; background-color: green; padding: 10px 20px; text-decoration: none; font-weight: 900; border-radius: 10px;">Sign In</a>
      ''')
  else:
    # If the request method is not POST, render the form
    return render(request, 'account_deletion.html')

def deactivate_account_confirmation(request):
  user_email = None  # Initialize user_email
  if 'user_id' in request.session:
    user_id = request.session['user_id']
    try:
      user = UserAccount.objects.get(id=user_id)  # Get the User instance
      user_email = user.email  # Get the user's email
    except UserAccount.DoesNotExist:
      print(f"No UserAccount found for id {user_id}")

  if request.method == 'POST':
    form = deactivateOtpForm(request.POST)
    if form.is_valid():
      entered_otp = form.cleaned_data.get('otp')
      if entered_otp == request.session.get('otp'):
        user.delete()
        logout(request)  # Log out the user
        return redirect('sign_in')
      else:
        # return HttpResponse("Invalid OTP or no user account. Sign in to your account...")
        form.add_error(None, mark_safe("Invalid OTP.. Enter a correct OTP and click the confirm button"))
  else:
    form = deactivateOtpForm()
  return render(request , 'delete_account_confirm.html', {'form': form, 'email': user_email})