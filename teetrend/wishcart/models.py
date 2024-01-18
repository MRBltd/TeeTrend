from django.db import models
from account.models import UserAccount
from catalog.models import Tshirt

class Wishlist(models.Model):
  user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
  tshirts = models.ManyToManyField(Tshirt)

  def __str__(self):
    return ", ".join([str(tshirt) for tshirt in self.tshirts.all()])

class Cart(models.Model):
  user = models.ForeignKey(UserAccount , on_delete=models.CASCADE)
  tshirts = models.ManyToManyField(Tshirt)    