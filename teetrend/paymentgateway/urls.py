from django.urls import path
from . import views

urlpatterns = [
  path('checkout/address/' , views.address , name='address') ,
  path('checkout/payment/' , views.payment , name='payment') ,
  path('checkout/make_payment/' , views.make_payment , name='make_payment') ,
]
