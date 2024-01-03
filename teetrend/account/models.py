from django.db import models

class UserAccount(models.Model):
  full_name = models.CharField(max_length=200)
  username = models.CharField(max_length=200 , unique=True)
  phone_number = models.CharField(max_length=15 , unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=128)
  otp = models.CharField(max_length=6 , blank=True, null=True)
  address = models.TextField(null=True , blank=True)
  birth_date = models.DateField(null=True, blank=True)
  is_verified = models.BooleanField(default=False)
  sign_in_timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.email