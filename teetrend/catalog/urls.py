from django.urls import path 
from . import views

urlpatterns = [
  path('' , views.product_catalog , name = 'product-catalog')
]