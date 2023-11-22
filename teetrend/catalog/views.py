from django.shortcuts import render
from django.http import HttpResponse
from .models import Tshirt , Category


def product_catalog(request):
  return HttpResponse("Hello..")

def mens_tshirts(request):
  mens_tshirts = Tshirt.objects.filter(category__categories=Category.MEN_TSHIRTS)
  return render(request , 'mens_t-shirts.html' , {'mens_tshirts' : mens_tshirts})

def womens_tshirts(request):
  womens_tshirts = Tshirt.objects.filter(category__categories=Category.WOMEN_TSHIRTS)
  return render(request , 'womens_t-shirts.html' , {'womens_tshirts' : womens_tshirts})

def kids_tshirts(request):
  return render(request , 'kids_t-shirts.html')

def characters_tshirts(request):
  return render(request , 'characters_t-shirts.html')