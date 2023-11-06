from django import forms
from .models import UserAccount
from django.contrib.auth import authenticate

class UserAccountForm(forms.ModelForm):
  class Meta:
    model = UserAccount
    fields = ['username', 'phone_number', 'email', 'password']
    widgets = {
      'password': forms.PasswordInput(),  
    }

class VerifyOTPForm(forms.Form):
  email = forms.EmailField()
  otp = forms.CharField(max_length=6)

class SignInForm(forms.Form):
  username = forms.CharField(max_length=200)
  password = forms.CharField(widget=forms.PasswordInput)

  # def clean(self):
  #   cleaned_data = super().clean()
  #   username = cleaned_data.get('username')
  #   password = cleaned_data.get('password')

  #   if username and password:
  #     self.user = authenticate(username=username , password=password)
  #   if self.user is None:
  #     raise forms.ValidationError('Invalid login credentials')