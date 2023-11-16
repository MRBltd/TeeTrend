from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserAccountForm , VerifyOTPForm , SignInForm , EmailSignInForm , SignInOtpForm
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


# The User entering details
def account(request):
  if 'user_id' in request.session:
    try:
      user_id = request.session['user_id']
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
      phone_number = form.cleaned_data.get('phone_number')
      email = form.cleaned_data.get('email')
      username = form.cleaned_data.get('username')
      # Check if the phone number, email, or username already exist in the database
      if UserAccount.objects.filter(phone_number=phone_number).exists():
        form.add_error('phone_number', 'This phone number is already in use')
      elif UserAccount.objects.filter(email=email).exists():
        form.add_error('email', 'This email is already in use')
      elif UserAccount.objects.filter(username=username).exists():
        form.add_error('username', 'This username is already in use')
      else:
        otp = generate_otp() # The Generated otp will saving in otp named variable
        user = form.save(commit=False)
        user.otp = otp
        user.save() # The otp saving in the database
        # The otp sending at user email
        send_mail(
          'Your OTP for Registration',
          f'Your OTP is: {otp}',
          'midhunbalachandran07@gmail.com',
          [email],
        )
        messages.success(request , f'Your User name is {username}')
        return redirect('verify_otp')
  else:
    form = UserAccountForm()
  return render(request, 'sign_up.html', {'form': form})

# The otp verification with email(the user enter the sign up email and otp for send the user email)
def verify_otp(request):
  if request.method == 'POST':
    form = VerifyOTPForm(request.POST)
    if form.is_valid():
      otp = form.cleaned_data.get('otp')
      email = form.cleaned_data.get('email')
      try:
        user = UserAccount.objects.get(email=email)
        if user.otp == otp:
          user.is_verified = True  # set is_verified to True
          user.save()  # save the change to the database
          request.session['user_id'] = user.id 
          messages.success(request, 'Welcome , Successful Logged')
          return redirect('home')
        else:
          form.add_error('otp', 'Invalid OTP')
      except UserAccount.DoesNotExist:
        form.add_error('email', 'No user with this email exists')
  else:
    form = VerifyOTPForm()
  return render(request , 'verify_otp.html' , {'form' : form})

# The user signin function (using username and password)
def sign_in(request):
  if request.method == 'POST':
    form = SignInForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      try:
        user = UserAccount.objects.get(username=username, password=password)
        request.session['user_id'] = user.id 
        messages.success(request, 'Welcome , Successful Logged')
        return redirect('home')
      except UserAccount.DoesNotExist:
        form.add_error(None, 'Invalid username or password')
  else:
    form = SignInForm()
  return render(request, 'sign_in.html', {'form': form})

# The siugi function using email
def email_sign_in(request):
  if request.method == 'POST':
    form = EmailSignInForm(request.POST)
    if form.is_valid():
      email = form.cleaned_data.get('email')
      try:
        user = UserAccount.objects.filter(email=email).first()
        if user:
          otp = generate_otp() # The Generated otp will saving in otp named variable
          user.otp = otp
          user.save() # The otp saving in the database
          # The otp sending at user email
          send_mail(
            'Your OTP',
            f'Your OTP is {otp}',
            'midhunbalachandran07@gmail.com',
            [user.email],
          )
          return redirect('sign_in_verify_otp')
      except UserAccount.DoesNotExist:
        form.add_error('email', 'No user with this email exists')
  else:
      form = EmailSignInForm()
  return render(request, 'email_sign_in.html', {'form': form})

# The Otp verification 
def sign_in_verify_otp(request):
  if request.method == 'POST':
    form = SignInOtpForm(request.POST)
    if form.is_valid():
      otp = form.cleaned_data.get('otp')
      email = form.cleaned_data.get('email')
      try:
        user = UserAccount.objects.get(otp=otp)
        if user.otp == otp:
          user.is_verified = True  
          user.save()  # save the change to the database
          request.session['user_id'] = user.id 
          messages.success(request, 'Welcome , Successful Logged')
          return redirect('home')
        else:
          form.add_error('otp', 'Invalid OTP')
      except UserAccount.DoesNotExist:
        form.add_error('email', 'No user with this email exists')
  else:
      form = SignInOtpForm()
  return render(request, 'sign_in_verify_otp.html', {'form': form})

# The User logout function
def logout_view(request):
  if 'user_id' in request.session:
      del request.session['user_id']
  return redirect('sign_in')

# The function for  User complete the signup or signin the home page will make some changes
def profile(request):
  # accts = None
  if 'user_id' in request.session:
    user_id = request.session['user_id']
    try:
      accts = UserAccount.objects.get(id=user_id)
    except UserAccount.DoesNotExist:
      pass
  return render(request, 'teetrend.html', {'accts': accts})  

def account_deletion_warning(request):
  return render(request , 'account_deletion.html')

# @login_required
def delete_account(request):
  sign_in_url = reverse('sign_in')
  if request.method == 'POST':
    if 'user_id' in request.session:
      return render(request , 'delete_account_confirm.html')
    else:
      return HttpResponse(f'''
      <h3>No user account. Sign in to your account...</h3>
      <a href="{sign_in_url}" style="color: white; background-color: green; padding: 10px 20px; text-decoration: none; font-weight: 900; border-radius: 10px;">Sign In</a>
      ''')
  else:
    # If the request method is not POST, render the form
    return render(request, 'account_deletion.html')

def delete_account_confirmation(request):
  if request.method == 'POST':
    if 'user_id' in request.session:
      user_id = request.session['user_id']
      try:
        user = UserAccount.objects.get(id=user_id)  # Get the User instance
        user.delete()
      except UserAccount.DoesNotExist:
        print(f"No UserAccount found for id {user_id}")
      logout(request)  # Log out the user
    else:
      return HttpResponse("No user account. Sign in to your account...")
    return redirect('sign_in')
  else:
    return render(request , 'delete_account_confirm.html')