from django.shortcuts import render
from django.http import HttpResponse


def product_catalog(request):
  return HttpResponse("Hello..")

def mens_tshirts(request):
  return render(request , 'mens_t-shirts.html')
