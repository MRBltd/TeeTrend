from django import forms
from .models import UserAccount

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