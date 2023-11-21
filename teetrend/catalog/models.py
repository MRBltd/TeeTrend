from django.db import models



class Category(models.Model):
  MEN_TSHIRTS = 'MT'
  WOMEN_TSHIRTS = 'WT'
  KIDS_TSHIRTS = 'KT'
  CHARACTERS = 'CH'

  CATEGORY_CHOICES = [
    (MEN_TSHIRTS, 'Men T-Shirts'),
    (WOMEN_TSHIRTS, 'Women T-Shirts'),
    (KIDS_TSHIRTS, 'Kids T-Shirts'),
    (CHARACTERS, 'Characters'),
  ]

  categories = models.CharField(
    max_length=2,
    choices=CATEGORY_CHOICES,
    default=MEN_TSHIRTS,
  )

  def __str__(self):
    return self.get_categories_display()
