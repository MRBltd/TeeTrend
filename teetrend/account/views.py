from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserAccountForm , VerifyOTPForm
from .models import UserAccount
from django.core.mail import send_mail
import random
import string


def account(request):
  return render(request , 'account_details.html')

def generate_otp(length=6):
  characters = string.digits
  otp = ''.join(random.choice(characters) for _ in range(length))
  print(otp)
  return otp

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
          # OTP is correct, add the success messages , redirect to the next page
          messages.success(request, 'Welcome , Successful Logged')
          return redirect('home')
        else:
          # OTP is incorrect, show an error message
          form.add_error('otp', 'Invalid OTP')
      except UserAccount.DoesNotExist:
        # Email does not exist, show an error message
        form.add_error('email', 'No user with this email exists')
  else:
    form = VerifyOTPForm()
  return render(request , 'verify_otp.html' , {'form' : form})