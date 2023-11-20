from django.shortcuts import render
from django.http import HttpResponse

def product_catalog(request):
  return HttpResponse('Hello ...')