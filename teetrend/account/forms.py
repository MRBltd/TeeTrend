from django import forms
from .models import UserAccount
from django.core.exceptions import ValidationError
import re

# The signup forms
class UserAccountForm(forms.ModelForm):
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input' , 'placeholder': 'Confirm Password'}))
  show_password = forms.BooleanField(required=False)
  class Meta:
    model = UserAccount
    fields = ['full_name' , 'username', 'phone_number', 'email', 'password' , 'confirm_password' , 'show_password']
    widgets = {
      'password': forms.PasswordInput(attrs={'class': 'password-input'}) ,  
    }
    widgets = {
        'full_name': forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'TeeTrend'}) ,
        'username': forms.TextInput(attrs={'class': 'text-input', 'placeholder': 'teetrend@info.123'}) ,
        'phone_number': forms.TextInput(attrs={'class': 'text-input', 'placeholder': '1234567890'}) ,
        'email': forms.EmailInput(attrs={'class': 'email-input', 'placeholder': 'teetrend@gmail.com'}) ,
        'password': forms.PasswordInput(attrs={'class': 'password-input', 'placeholder': 'Password'}) ,  
      }

  def clean_password(self):
    password = self.cleaned_data.get('password')
    full_name = self.cleaned_data.get('full_name')
    username = self.cleaned_data.get('username')
    email = self.cleaned_data.get('email')
    phone_number = self.cleaned_data.get('phone_number')

    # Checking the password have atleast 8 characters
    if len(password) < 8:
      raise ValidationError("Password must be at least 8 characters long.")

    # Checking the password include some special characters
    if not re.search(r'\W', password):
      raise ValidationError("Password must include at least one special character.")

    # Checking the password not to the similar to personal details
    if (full_name and full_name in password) or (username and username in password) or (email and email in password) or (phone_number and phone_number in password):
        raise ValidationError("Password should not contain your personal information such as full name, username, email, or phone number.")  
        
    return password

  def clean(self):
    cleaned_data = super().clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')

    # Checking the password and confirm password has same
    if password != confirm_password:
      self.add_error('confirm_password', 'Password and confirm password does not match')

# The OTP verification with email forms
class VerifyOTPForm(forms.Form):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'teetrend@gmail.com'}))
  otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': '0 0 0 0 0 0'}))

# The User signin forms
class SignInForm(forms.Form):
  username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'teetrend@info.123'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'password-input', 'placeholder': 'Password'}))
  show_password = forms.BooleanField(required=False)

# The User signin forms using email
class EmailSignInForm(forms.Form):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'teetrend@gmail.com'}))

# The otp verification
class SignInOtpForm(forms.Form):
  otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': '0 0 0 0 0 0'}))

class deactivateOtpForm(forms.Form):
  otp = forms.CharField(max_length=6 , widget=forms.TextInput(attrs={'placeholder': '0 0 0 0 0 0'}))

class DateInput(forms.DateInput):
  input_type = 'date'

class EditProfileForm(forms.ModelForm):
  birth_date = forms.DateField(widget=DateInput)
  password = forms.CharField(widget=forms.PasswordInput, required=False)
  show_password = forms.BooleanField(required=False)
  
  class Meta:
    model = UserAccount
    fields = ['full_name','username', 'phone_number', 'email', 'password' , 'show_password' , 'address', 'birth_date']

  def clean_password(self):
    password = self.cleaned_data.get('password')
    full_name = self.cleaned_data.get('full_name')
    username = self.cleaned_data.get('username')
    email = self.cleaned_data.get('email')
    phone_number = self.cleaned_data.get('phone_number')

    # Checking the password have atleast 8 characters
    if len(password) < 8:
      raise ValidationError("Password must be at least 8 characters long.")

    # Checking the password include some special characters
    if not re.search(r'\W', password):
      raise ValidationError("Password must include at least one special character.")

    # Checking the password not to the similar to personal details
    if (full_name and full_name in password) or (username and username in password) or (email and email in password) or (phone_number and phone_number in password):
      raise ValidationError("Password should not contain your personal information such as full name, username, email, or phone number.")  
        
    return password
