from django.urls import path 
from . import views

urlpatterns = [
  path('' , views.account , name='account') ,
  path('sign_up/' , views.sign_up , name='sign_up') ,
  path('verify_otp/' , views.verify_otp , name = 'verify_otp') ,
]