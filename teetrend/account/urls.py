from django.urls import path 
from . import views

urlpatterns = [
  path('account/' , views.account , name='account') ,
  path('account/sign_up/' , views.sign_up , name='sign_up') ,
]