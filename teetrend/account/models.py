from django.db import models


class UserAccount(models.Model):
  username = models.CharField(max_length=200 , unique=True)
  phone_number = models.CharField(max_length=15 , unique=True)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=128)
  otp = models.CharField(max_length=6)
