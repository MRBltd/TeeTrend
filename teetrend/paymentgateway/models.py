from django.db import models
from account.models import UserAccount


class Payment(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  status = models.CharField(max_length=20)