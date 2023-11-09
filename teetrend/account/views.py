from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserAccountForm , VerifyOTPForm , SignInForm
from .models import UserAccount
from django.core.mail import send_mail
import random
import pyotp
import string
from django.contrib.auth import login , authenticate , logout


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

def generate_otp(length=6):
  base32secret = pyotp.random_base32()
  otp = pyotp.TOTP(base32secret, interval=60, digits=6)
  print(otp)
  return otp.now()

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
        otp = generate_otp()
        user = form.save(commit=False)
        user.otp = otp
        user.save()
        # request.session['user_id'] = user.id
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

def logout_view(request):
  if 'user_id' in request.session:
      del request.session['user_id']
  return redirect('home')

def profile(request):
  if 'full_name' in request.session:
    full_name = request.session['full_name']
    accts = UserAccount.objects.get(full_name=full_name)  
    return render(request, 'teetrend.html', {'accts': accts})