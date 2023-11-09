from django import forms
from .models import UserAccount
from django.core.exceptions import ValidationError
import re

class UserAccountForm(forms.ModelForm):
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input'}))
  class Meta:
    model = UserAccount
    fields = ['full_name' , 'username', 'phone_number', 'email', 'password' , 'confirm_password']
    widgets = {
      'password': forms.PasswordInput(attrs={'class': 'password-input'}),  
    }

  def clean_password(self):
    password = self.cleaned_data.get('password')
    full_name = self.cleaned_data.get('full_name')
    username = self.cleaned_data.get('username')
    email = self.cleaned_data.get('email')
    phone_number = self.cleaned_data.get('phone_number')

    if len(password) < 8:
      raise ValidationError("Password must be at least 8 characters long.")

    if not re.search(r'\W', password):
      raise ValidationError("Password must include at least one special character.")

    if (full_name and full_name in password) or (username and username in password) or (email and email in password) or (phone_number and phone_number in password):
        raise ValidationError("Password should not contain your personal information such as full name, username, email, or phone number.")  
        
    return password

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')

    if password != confirm_password:
      self.add_error('confirm_password', 'Password and confirm password does not match')  

class VerifyOTPForm(forms.Form):
  email = forms.EmailField()
  otp = forms.CharField(max_length=6)

class SignInForm(forms.Form):
  username = forms.CharField(max_length=200)
  password = forms.CharField(widget=forms.PasswordInput)
