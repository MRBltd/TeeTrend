from django.shortcuts import render
from django.http import HttpResponse


def product_catalog(request):
  return HttpResponse("Hello..")

def mens_tshirts(request):
  return render(request , 'mens_t-shirts.html')

def womens_tshirts(request):
  return render(request , 'womens_t-shirts.html')

def kids_tshirts(request):
  return render(request , 'kids_t-shirts.html')

def characters_tshirts(request):
  return render(request , 'characters_t-shirts.html')