from django.urls import path 
from . import views

urlpatterns = [
  path('' , views.account , name='account') , # The account urls
  path('sign_up/' , views.sign_up , name='sign_up') , # The signup urls
  path('verify_otp/' , views.verify_otp , name = 'verify_otp') , # The otp verification with email urls
  path('sign_in/' , views.sign_in , name = 'sign_in') , # The sigin urls
  path('email_sign_in/' , views.email_sign_in , name = 'email_sign_in') , # The email signin urls
  path('sign_in_verify_otp/' , views.sign_in_verify_otp , name = 'sign_in_verify_otp') , # The signin otp verification urls
  path('logout/' , views.logout_view , name = 'logout') , # The logout urls
  path('Warning_account_Deletion/' , views.account_deletion_warning , name = 'account_deletion_warning') , # The User Account Deletion warning messages
  path('delete_account/', views.delete_account, name='delete_account') , # The User account deleting urls
  path('delete_account_confirmation/' , views.delete_account_confirmation , name = 'delete_account_confirmation') , # The User account deletion confirmation
  path('profile_overview/' , views.profileOverview , name = 'priofile_overview') , # The profile overview urls
]