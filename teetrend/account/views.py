from django.shortcuts import render
from django.http import HttpResponse


def account(request):
  return render(request , 'account_details.html')

def sign_up(request):
  return render(request , 'sign_up.html')  